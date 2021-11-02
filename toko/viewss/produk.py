from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from django.contrib import messages
from toko.models import *
from toko.form import *

# Create your views here.
def produk(request):
    produk = Product.objects.all()

    konteks={'produks':produk}

    return render(request, 'produk/produk.html', konteks)

def hapus_produk(request, id_produk):
    produk = Product.objects.filter(id=id_produk)
    produk.delete()

    return redirect('produk')

def ubah_produk(request, id_produk):
    produk = Product.objects.get(id = id_produk)

    if request.POST:
        form = FormProduk(request.POST,instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diubah')

            return redirect('ubah_produk',id_produk)
        else :
            messages.error(request, 'Produk berhasil diubah')
            return redirect('ubah_produk',id_produk)
    else:
        form = FormProduk(instance=produk)

        konteks={
            'produk':produk,
            'form':form
        }

        return render(request, 'produk/ubah_produk.html', konteks)

def tambah_produk(request):
    if request.POST:
        form = FormProduk(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambah')

            return redirect('tambah_produk')
        else :
            messages.error(request, 'Produk berhasil ditambah')
            return redirect('tambah_produk')

    else :
        form = FormProduk()

        konteks={
            'form':form
        }

        return render(request, 'produk/tambah_produk.html',konteks)
# def superUser(request):
#     pass

def beli_produk(request,id_produk):
    produk = Product.objects.get(id=id_produk)
    form = FormProduk( instance=produk)
    
    instance = form.save(commit=False)
    instance.jumlah -= 1

    instance.save()
    return redirect('produk')




