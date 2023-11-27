from django.db import models
from django.utils.text import slugify


# Create your models here.


class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    kategoriResim = models.FileField(upload_to='kategoripic/')
    slug = models.SlugField(null= True , unique=True , db_index=True , blank=True , editable=False)
    backImage = models.FileField(upload_to='backgroundkategoripic/')

    def save(self, *args , **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.isim
    

class Urun(models.Model):
    urunKodu = models.CharField(max_length=50)
    urunKategori = models.ForeignKey(Kategori , on_delete=models.CASCADE , null=True)
    slug = models.SlugField(null=True , unique=True , db_index=True,blank=True,editable=False)
    urunResim = models.FileField(upload_to='urunpic/')
    kanat = models.TextField(max_length=2000)
    kasa = models.TextField(max_length=2000)
    pervaz = models.TextField(max_length=2000)
    cila = models.TextField(max_length=2000 , null=True , blank=True)
    boya = models.TextField(max_length=2000 , null=True , blank=True)

    def save(self, *args , **kwargs):
        self.slug = slugify(self.urunKodu)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.urunKodu
    
class FabrikaImg(models.Model):
    image = models.FileField(upload_to='fabrikapic/')
    def __str__(self):
        return self.image.url


class FuarImg(models.Model):
    image = models.FileField(upload_to='fuarpic/')
    def __str__(self):
        return self.image.url
