from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
import translation
  
from .models import Image, Logo
 
class ImageAdmin(TranslationAdmin):
    list_display = ["id", "title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]
    class Meta:
        model = Image

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class LogoModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]
    class Meta:
        model = Logo
 
 
admin.site.register(Image, ImageAdmin)
admin.site.register(Logo, LogoModelAdmin)