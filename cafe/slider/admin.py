from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import MainBanner, Banners


# Баннера слайдра в админке
class BannersInline(admin.TabularInline):
    model = Banners
    extra = 1


# Слайдер в админке
@admin.register(MainBanner)
class IndexAdminForm(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'button_title']
    inlines = [BannersInline]
