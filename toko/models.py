from django.db import models

# Create your models here.
class Tag(models.Model):
    nama = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.nama

class Kategori(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self) :
        return self.nama


class Product(models.Model):
    nama = models.CharField(max_length=50, null=True)
    jumlah = models.IntegerField(null=True)
    keterangan = models.TextField(null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    harga_beli = models.IntegerField(null=True)
    harga_jual = models.IntegerField(null=True)
    harga_promo = models.IntegerField(null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) :
        return self.nama