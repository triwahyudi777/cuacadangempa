from django.contrib import admin
from cuaca.models import *

# Register your models here.

admin.site.register(Kategori)

class ArtikelAdmin (admin.ModelAdmin):
    list_display = ('nama','judul',  'isi', 'kategori')

admin.site.register(Artikel, ArtikelAdmin)

class GempaAdmin (admin.ModelAdmin):
    list_display = ('tanggal', 'jam', 'date_time', 'coordinates', 'lintang', 'bujur', 'magnitudo', 'kedalaman', 'wilayah', 'potensi','dirasakan','shakemap')

admin.site.register(Gempa, GempaAdmin)

class CuacaAdmin (admin.ModelAdmin):
    list_display = ('id', 'propinsi', 'kota', 'kecamatan', 'lat', 'lon')

admin.site.register(Cuaca, CuacaAdmin)



