from django.urls import path
from . import views


urlpatterns = [

 path('' , views.index , name='index'),
 path("kategori/<str:slug>" , views.kategori , name="kategori"),
 path('hakkimizda/' , views.hakkimizda , name='hakkimizda'),
 path('iletisim/' , views.iletisim , name='iletisim'),
 path('fabrikadan/' , views.fabrika , name='fabrikadan'),
 path('fuarlardan/' , views.fuar , name='fuarlardan'),
 path('urundetay/<str:slug>' , views.urunDetay , name='urundetay'),
 path('search/' , views.search , name='search')
]