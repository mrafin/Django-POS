from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from django.contrib import messages
from toko.models import *
from toko.form import *

# Create your views here.
def kategori(request):
    kategori = Kategori.objects.all()

    konteks={'kategoris':kategori}

    return render(request, 'kategori/kategori.html', konteks)

def hapus_kategori(request, id_kategori):
    kategori = Kategori.objects.filter(id=id_kategori)
    kategori.delete()

    return redirect('kategori')

def ubah_kategori(request, id_kategori):
    kategori = Kategori.objects.get(id = id_kategori)

    if request.POST:
        form = FormKategori(request.POST,instance=kategori)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil diubah')

            return redirect('ubah_kategori',id_kategori)
        else :
            messages.error(request, 'Kategori berhasil diubah')
            return redirect('ubah_kategori',id_kategori)
    else:
        form = FormKategori(instance=kategori)

        konteks={
            'kategori':kategori,
            'form':form
        }

        return render(request, 'kategori/ubah_kategori.html', konteks)

def tambah_kategori(request):
    if request.POST:
        form = FormKategori(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil ditambah')

            return redirect('tambah_kategori')
        else :
            messages.error(request, 'Kategori berhasil ditambah')
            return redirect('tambah_kategori')

    else :
        form = FormKategori()

        konteks={
            'form':form
        }

        return render(request, 'kategori/tambah_kategori.html',konteks)
# def superUser(request):
#     pass