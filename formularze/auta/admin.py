from django.contrib import admin
from .models import Auto
# Register your models here.

@admin.register(Auto)
class AdminAuto(admin.ModelAdmin):
    pass

#admin.site.register(Auto)