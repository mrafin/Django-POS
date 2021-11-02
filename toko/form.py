from django.db.models import fields
from django.forms import ModelForm
from toko.models import *

class FormTag(ModelForm):
    class Meta:
        model=Tag
        fields='__all__'

class FormKategori(ModelForm):
    class Meta :
        model = Kategori
        fields = '__all__'

class FormProduk(ModelForm):
    class Meta :
        model = Product
        fields = '__all__'



        