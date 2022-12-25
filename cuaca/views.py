from django.http import request 
from django.shortcuts import render, redirect
from multiprocessing import context
from cuaca.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
import requests
from .forms import ArtikelForms


def is_creator(user):
    if user.groups.filter(name='Creator').exists():
        return True
    else:
        return False

def sinkron_gempa(request):
	url = "https://cuaca-gempa-rest-api.vercel.app/quake"
	data = requests.get(url).json()
	for d in data:
		cek_berita = Gempa.objects.filter(wilayah=d['wilayah'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.wilayah=d['wilayah']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Gempa.objects.create(
				tanggal = d['tanggal'],
				jam = d['jam'],
				date_time = d['dateTime'],
				coordinates = d['coordinates'],
				lintang = d['lintang'],
				bujur = d['bujur'],
				magnitudo = d['magnitudo'],
				kedalaman = d['kedalamaan'],
				wilayah = d['wilayah'],
                potensi = d['potensi'],
                dirasakan = d['dirasakan'],
                shakemap = d['shakemap'],
			)
	return redirect(gempa)
def sinkron_cuaca(request):
	url = "https://ibnux.github.io/BMKG-importer/cuaca/wilayah.json"
	data = requests.get(url).json()
	for d in data:
		cek_berita = Cuaca.objects.filter(id=d['id'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.id=d['id']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Cuaca.objects.create(
				id = d['id'],
				propinsi = d['propinsi'],
				kota = d['kota'],
				kecamatan = d['kecamatan'],
				lat = d['lat'],
				lon = d['lon'],
			)
	return redirect(cuaca)
# def gempa(request):
#     url = "https://cuaca-gempa-rest-api.vercel.app/quake"

#     data = requests.get(url).json()

#     a = data['data']
#     tanggal = []
#     jam = []
#     datetime = []
#     kordinat = []
#     lintang =[]
#     bujur = []
#     magnitude = []
#     kedalaman = []
#     wilayah = []
#     potensi = []
#     shakemap = []

#     for i in range(len(a)):
#         f = a[i]
#         tanggal.append(f['tanggal'])
#         jam.append(f['jam'])
#         datetime.append(f['dateTime'])
#         kordinat.append(f['coordinates'])
#         lintang.append(f['lintang'])
#         bujur.append(f['bujur'])
#         magnitude.append(f['magnitude'])
#         kedalaman.append(f['kedalaman'])
#         wilayah.append(f['wilayah'])
#         potensi.append(f['potensi'])
#         shakemap.append(f['shakemap'])

#     mylist = zip(tanggal,jam,datetime,kordinat
#     ,lintang,bujur,magnitude,kedalaman,wilayah,potensi)
#     context ={'mylist':mylist}

#     return render(request, 'back/table_gempa.html', context)
@login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
         request.session['is_creator'] = 'creator'
         

        
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard'
    }
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/table_artikel.html"
    artikel = Artikel.objects.all()
    # for a in artikel:
    #     print(a.id, '-', a.id, '-' , a.lat)
    context = {
        'title' : 'dashboard',
        'artikel' : artikel,
    }
    return render(request, template_name, context)


@login_required
@user_passes_test(is_creator)
def users(request):
    template_name = "back/table_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)





@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        forms_artikel  = ArtikelForms(request.POST)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect (artikel)
    else:
        forms_artikel = ArtikelForms()
        
    context = {
        'title' : 'dashboard',
        'kategori' : kategori,
        'forms_artikel' : forms_artikel
    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id) 
    context = {
        'title' : 'lihat artikel',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
    template_name = 'back/tambah_artikel.html'
   
    a = Artikel.objects.get(id = id)
    if request.method == "POST":

        forms_artikel  = ArtikelForms(request.POST, instance=a)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect (artikel)
    else:
        forms_artikel = ArtikelForms()
        
    context = {
        'title' : 'Edit Artikel',
        'artikel' : a,
        'forms_artikel' : forms_artikel,
    }
    return render (request, template_name, context)

@login_required
def hapus_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

Gempa
@login_required
def cuaca(request):
    template_name = "back/table_cuaca.html"
    cuaca = Cuaca.objects.all()
    # for a in artikel:
    #     print(a.id, '-', a.id, '-' , a.lat)
    context = {
        'title' : 'dashboard',
        'cuaca' : cuaca,
    }
    return render(request, template_name, context)

def gempa(request):
    template_name = "back/table_gempa.html"
    gempa = Gempa.objects.all()
    # for a in artikel:
    #     print(a.id, '-', a.id, '-' , a.lat)
    context = {
        'title' : 'dashboard',
        'gempa' : gempa,
    }
    return render(request, template_name, context)

@login_required
def tambah_cuaca(request):
    template_name = "back/tambah_cuaca.html"
    lat = lat.objects.all()
    if request.method == "POST":
        id = request.POST.get('id')
        propinsi = request.POST.get('propinsi')
        kota = request.POST.get('kota')
        kecamatan = request.POST.get('kecamatan')
        lat = request.POST.get('lat')

        kat = lat.objects.get(nama=lat)

        Cuaca.objects.create(
            id = id,
            propinsi = propinsi,
            kota = kota,
            kecamatan = kecamatan,
            lat= kat,
        )
        return redirect(cuaca)
    context = {
        'title' : 'dashboard',
        'lat' : lat,
    }
    return render(request, template_name, context)

@login_required
def lihat_cuaca(request, id):
    template_name = "back/lihat_cuaca.html"
    cuaca = Cuaca.objects.get(id=id) 
    context = {
        'title' : 'lihat cuaca',
        'cuaca' : cuaca,
    }
    return render(request, template_name, context)

@login_required
def edit_cuaca(request, id):
    template_name = 'back/edit_cuaca.html'
   
    a = Cuaca.objects.get(id = id)
    if request.method == "POST":
        id = request.POST.get('id')
        propinsi = request.POST.get('propinsi')
        kota = request.POST.get('kota')
        kecamatan = request.POST.get('kecamatan')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        #input lat

        #simpan produk karena ada relasi ke tabel lat
        a.id = id
        a.propinsi = propinsi
        a.kota = kota
        a.kecamatan = kecamatan
        a.lat = lat
        a.lon= lon
        
        a.save()
        return redirect(cuaca)
    context = {
        'title' : 'Edit Artikel',
        'cuaca' : cuaca,
    }
    return render (request, template_name, context)

@login_required
def hapus_cuaca(request,id):
    Cuaca.objects.get(id=id).delete()
    return redirect(cuaca)






# Create your views here.

# def barang_add(request):
#     template_name = 'barang_add.html'
#     lat = lat.objects.all()
#     if request.method == "POST":

#         input_lat = request.POST.get('lat')
#         input_id = request.POST.get('id')
#         input_propinsi = request.POST.get('propinsi')
#         input_kota = request.POST.get('kota')
#         input_kecamatan = request.POST.get('kecamatan')

#         #input lat Dulu
#         get_lat = lat.objects.get(nama=input_lat)

#         #simpan produk karena ada relasi ke tabel lat 
#         Produk.objects.create(
#             id = input_id,
#             propinsi = input_propinsi,
#             kota = input_kota,
#             kecamatan = input_kecamatan,
#             lat = get_lat,
#         )
#         return redirect(barang_list)
#     context = {
#         'title':'my home',
#         'lat':lat

#     }
#     return render(request, template_name, context)