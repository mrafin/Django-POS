from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from django.contrib import messages
from toko.models import *
from toko.form import *

# Create your views here.
def tag(request):
    tag = Tag.objects.all()

    konteks={'tags':tag}

    return render(request, 'tag/tag.html', konteks)

def hapus_tag(request, id_tag):
    tag = Tag.objects.filter(id=id_tag)
    tag.delete()

    return redirect('tag')

def ubah_tag(request, id_tag):
    tag = Tag.objects.get(id = id_tag)

    if request.POST:
        form = FormTag(request.POST,instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag berhasil diubah')

            return redirect('ubah_tag',id_tag)
        else :
            messages.error(request, 'Tag berhasil diubah')
            return redirect('ubah_tag',id_tag)
    else:
        form = FormTag(instance=tag)

        konteks={
            'tag':tag,
            'form':form
        }

        return render(request, 'tag/ubah_tag.html', konteks)

def tambah_tag(request):
    if request.POST:
        form = FormTag(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag berhasil ditambah')

            return redirect('tambah_tag')
        else :
            messages.error(request, 'Tag berhasil ditambah')
            return redirect('tambah_tag')

    else :
        form = FormTag()

        konteks={
            'form':form
        }

        return render(request, 'tag/tambah_tag.html',konteks)
# def superUser(request):
#     pass