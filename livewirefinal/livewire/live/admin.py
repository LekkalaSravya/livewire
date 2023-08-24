from django.contrib import admin
from .models import *
class LivedataAdmin(admin.ModelAdmin):
    list_display=('name','des1','intro_img','duration','name2','des2','objective','keytopic1','keytopic2','scope','range2','projectexp')

admin.site.register(Livedata,LivedataAdmin)
# Register your models here.
