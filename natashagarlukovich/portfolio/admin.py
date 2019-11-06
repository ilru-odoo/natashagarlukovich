from django.contrib import admin
  
from .models import Image, Logo
 
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]
    class Meta:
        model = Image

class LogoModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]
    class Meta:
        model = Logo
 
 
admin.site.register(Image, ImageModelAdmin)
admin.site.register(Logo, LogoModelAdmin)