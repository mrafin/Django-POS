from django.contrib import admin
from django.urls import path
from toko.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('superUser/', superUser , name='superUser' )
    path('tag/', tag, name='tag'),
    path('tambah-tag/', tambah_tag, name='tambah_tag'),
    path('ubah-tag/<int:id_tag>', ubah_tag, name='ubah_tag'),
    path('hapus-tag/<int:id_tag>',hapus_tag,name='hapus_tag'),
    
    path('kategori/', kategori, name='kategori'),
    path('tambah-kategori/', tambah_kategori, name='tambah_kategori'),
    path('ubah-kategori/<int:id_kategori>', ubah_kategori, name='ubah_kategori'),
    path('hapus-kategori/<int:id_kategori>',hapus_kategori,name='hapus_kategori'),

    path('produk/', produk, name='produk'),
    path('tambah-produk/', tambah_produk, name='tambah_produk'),
    path('ubah-produk/<int:id_produk>', ubah_produk, name='ubah_produk'),
    path('hapus-produk/<int:id_produk>',hapus_produk,name='hapus_produk'),
    path('beli-produk/<int:id_produk>',beli_produk,name='beli_produk'),
]
