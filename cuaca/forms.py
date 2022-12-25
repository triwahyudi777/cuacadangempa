from django import forms
from .models import Artikel
from django.forms import widgets

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'placeholder':"judul Artikel",
                    'required' : True
                }),
            "isi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols' : "30",
                    'rows' : "10",
                    'required' : True
                }),
            "kategori" : forms.Select(
                attrs={
                    'class' : 'form-control selectpicker',
                    'type' : 'text',
                    'required' : True,
                    'data-style' :'btn btn-danger btn-block',
                    'title' : 'Pilih kategori',
                    'data-size':'7',


                }),
            
        }