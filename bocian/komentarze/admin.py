from django.contrib import admin
from .models import Komentarz

# Register your models here.

@admin.register(Komentarz)
class AdminKomentarz(admin.ModelAdmin):
    pass
