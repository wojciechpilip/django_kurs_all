from django.contrib import admin

# Register your models here.

from .models import Komentarz

@admin.register(Komentarz)
class AdminKomentarz(admin.ModelAdmin):
    pass