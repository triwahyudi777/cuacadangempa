from cuaca.models import Artikel, Gempa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password

from cuaca.models import Artikel,Cuaca
from users.models import Biodata
import requests

def home(request):
    template_name = 'front/home.html'
    context = {
        'title': 'ini adalah halaman index'
    }
    return render(request, template_name, context)
    
def about(request):
    template_name = 'front/blog-posts.html'
    context = {
        'title': 'ini adalah halaman about'
    }
    return render(request, template_name, context)

def artikel(request):
    template_name = 'front/artikel.html'
    artikel = Artikel.objects.all()
    context = {
        'title': 'ini adalah halaman artikel',
        'artikel' : artikel,
    }
    return render(request, template_name, context)


def cuaca(request):
    template_name = 'front/cuaca.html'
    cuaca = Cuaca.objects.all()
    context = {
        'title': 'ini adalah halaman cuaca',
        'cuaca' : cuaca,
    }
    return render(request, template_name, context)

def about_us(request):
    template_name = 'front/about-us.html'
    context = {
        'title': 'ini adalah halaman about'
    }
    return render(request, template_name, context)

# def gempa(request):
#     template_name = 'front/gempa.html'
#     gempa = Gempa.objects.all()
#     context = {
#         'title': 'ini adalah halaman gempa',
#         'gempa' : gempa,
#     }
#     return render(request, template_name, context)

def contact_us(request):
    template_name = 'front/contact-us.html'
    context = {
        'title': 'ini adalah halaman about'
    }
    return render(request, template_name, context)

def detail(request, id):
    template_name = 'front/detail.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        'title': 'ini adalah halaman c',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

def g(request):
    template_name = 'front/g.html'
    gempa = Gempa.objects.all()
    context = {
        'title': 'ini adalah halaman g',
        'gempa' : gempa,
    }
    return render(request, template_name, context)

    #LOGIN
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'accounts/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('home')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
    
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    template_name = 'accounts/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)

def gempa(request):
    url = "https://cuaca-gempa-rest-api.vercel.app/quake"

    data = requests.get(url).json()

    a = data['data']
    tanggal = []
    jam = []
    datetime = []
    kordinat = []
    lintang =[]
    bujur = []
    magnitude = []
    kedalaman = []
    wilayah = []
    potensi = []
    shakemap = []

    for i in range(len(a)):
        f = a
        tanggal.append(f['tanggal'])
        jam.append(f['jam'])
        datetime.append(f['datetime'])
        kordinat.append(f['coordinates'])
        lintang.append(f['lintang'])
        bujur.append(f['bujur'])
        magnitude.append(f['magnitude'])
        kedalaman.append(f['kedalaman'])
        wilayah.append(f['wilayah'])
        potensi.append(f['potensi'])
        shakemap.append(f['shakemap'])

    mylist = zip(tanggal,jam,datetime,kordinat
    ,lintang,bujur,magnitude,kedalaman,wilayah,potensi,shakemap)
    context ={'mylist':mylist}

    return render(request, 'front/gempa.html', context)