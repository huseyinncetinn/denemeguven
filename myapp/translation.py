from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Kategori)
class KategoriTranslationOption(TranslationOptions):
    fields = ('isim',)


@register(Urun)
class KategoriTranslationOption(TranslationOptions):
    fields = ('urunKodu', 'kanat' , 'kasa' , 'pervaz' , 'cila' , 'boya')