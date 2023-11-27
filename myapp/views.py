from django.shortcuts import render , get_object_or_404 ,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q



# Create your views here.

def search(request):

    kategoriler = Kategori.objects.all()

    urunler = ''
    searched = ''

    if request.GET.get('searched'):
        searched = request.GET['searched']
        urunler = Urun.objects.filter(
            Q(urunKodu__contains = searched) |
            Q(urunKategori__isim__contains = searched)
        )
    context = {
        'urunler' : urunler,
        'kategoriler' : kategoriler

    }
    return render ( request , 'search.html' , context)

def index(request):
    kategoriler = Kategori.objects.all()
    context = {
        'kategoriler' : kategoriler
    }
    return render(request , 'index.html' ,context)

def kategori(request , slug):
    kategoriler = Kategori.objects.all()
    kategori = get_object_or_404(Kategori , slug = slug)
    urunler = Urun.objects.filter( urunKategori = kategori)

    page = Paginator(urunler , 12)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    context = {
        'page' : page,
        'kategoriler' : kategoriler ,
        'kategori' : kategori ,
        "link" : "kategori/"+str(slug),
        'urunler' : urunler

    }
    return render(request,'kategori.html' , context)

def urunDetay(request , slug):
    kategoriler = Kategori.objects.all()
    urun = get_object_or_404(Urun , slug = slug)
    context = {
        'urun' : urun,
        "link" : "urundetay/"+str(slug),
        'kategoriler' : kategoriler ,

    }
    return render(request,'urundetay.html',context)

def hakkimizda(request):
    kategoriler = Kategori.objects.all()

    context = {
        'kategoriler' : kategoriler ,

        "link" : "hakkimizda/"
    }
    return render(request, 'hakkimizda.html' , context)

def iletisim(request):
    kategoriler = Kategori.objects.all()

    context = {
        'kategoriler' : kategoriler ,

        "link" : "iletisim/"
    }
    return render(request, 'iletisim.html' , context)

def fabrika(request):
    kategoriler = Kategori.objects.all()
    resimler = FabrikaImg.objects.all()
    context = {
        'kategoriler' : kategoriler ,
        "link" : "fabrikadan/",
        'resimler' : resimler
    }

    return render(request , 'fabrika.html',context)

def fuar(request):
    kategoriler = Kategori.objects.all()
    resimler = FuarImg.objects.all()

    context = {
        'kategoriler' : kategoriler ,
        "link" : "fuarlardan/",
        'resimler' : resimler
    }

    return render(request , 'fuar.html',context)

def view_404(request , exception):
    return render (request , '404.html')