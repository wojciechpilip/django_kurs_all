from django.contrib import admin

# Register your models here.

from .models import Wpis, Tag

class AdminWpis(admin.ModelAdmin):
    list_display = ['id', 'tytul','created', 'modified']
    search_fields = ['tytul', 'tresc']
    readonly_fields = ['created', 'modified']


admin.site.register(Wpis, AdminWpis)

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass