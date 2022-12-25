from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.shortcuts import render

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.

#cekeditor
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
         return self.nama

    class Meta:
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.ForeignKey(User,on_delete=models.CASCADE,blank= True, null=True)
    judul = models.CharField(max_length=100)
    isi = models.TextField(blank= True, null=True )              
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    
    def __str__(self):
        return "{} - {}".format(self.judul, self.judul)

class Meta:
    ordering = ['-id']
    verbose_nama_plural = "Artikel"


class Gempa(models.Model):
    tanggal = models.TextField(max_length=255, blank=True,null=True)
    jam = models.CharField(max_length=100,blank=True,null=True)
    date_time = models.DateTimeField(blank=True,null=True),
    coordinates = models.CharField(max_length=100, blank=True,null=True)
    lintang = models.CharField(max_length=100, blank=True,null=True)
    bujur = models.CharField(max_length=100, blank=True,null=True)
    magnitudo = models.CharField(max_length=100, blank=True,null=True)
    kedalaman = models.CharField(max_length=100, blank=True,null=True)
    wilayah = models.TextField(blank=True,null=True)
    potensi = models.TextField(blank=True,null=True)
    dirasakan = models.CharField(max_length=100,blank=True,null=True)
    shakemap = models.CharField(max_length=1000,blank=True,null=True)
    
    
    def __str__(self):
        return "{} - {}".format(self.tanggal, self.tanggal)

class Meta:
    ordering = ['-id']
    verbose_nama_plural = "Gempa"

class Cuaca(models.Model):
    id = models.IntegerField(primary_key=True)
    propinsi = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.id, self.id)


    


    

