from django.contrib import admin
from myapp.models import *

class KategoriAdmin(admin.ModelAdmin):
    list_display = ( 'isim' ,'slug',)
    readonly_fields = ('slug',)

class UrunAdmin(admin.ModelAdmin):
    list_display = ( 'urunKodu' ,'slug',)
    readonly_fields = ('slug',)

# Register your models here.

admin.site.register(Kategori , KategoriAdmin)
admin.site.register(Urun , UrunAdmin) 
admin.site.register(FabrikaImg)
admin.site.register(FuarImg)



