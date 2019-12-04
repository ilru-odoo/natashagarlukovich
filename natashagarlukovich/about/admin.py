from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
import translation
 
# Register your models here.
 
from .models import AboutPost
 

class AboutPostAdmin(TranslationAdmin):
    list_display = ["id" ,"title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = AboutPost

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

 
admin.site.register(AboutPost, AboutPostAdmin)