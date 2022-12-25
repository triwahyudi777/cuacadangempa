from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('artikel',artikel, name='table_artikel'),
    path('users',users, name='table_users'),
    path('artikel/tambah_artikel',tambah_artikel, name='tambah_artikel'),
    path('artikel/lihat/<str:id>',lihat_artikel, name='lihat_artikel'),
    path('artikel/edit/<str:id>',edit_artikel, name='edit_artikel'),
    path('artikel/hapus/<str:id>',hapus_artikel, name='hapus_artikel'),
    path('cuaca', cuaca, name='table_cuaca'),
    path('gempa', gempa, name='table_gempa'),
    path('cuaca/tambah_cuaca',tambah_cuaca, name='tambah_cuaca'),
    path('cuaca/lihat/<str:id>',lihat_cuaca, name='lihat_cuaca'),
    path('cuaca/edit/<str:id>',edit_cuaca, name='edit_cuaca'),
    path('cuaca/hapus/<str:id>',hapus_cuaca, name='hapus_cuaca'),
    path('sinkron_cuaca', sinkron_cuaca, name='sinkron_cuaca'),
    path('sinkron_gempa', sinkron_gempa, name='sinkron_gempa'),

    
]
