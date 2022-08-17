from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import MainBanner, Banners


class BannersInline(admin.TabularInline):
    model = Banners
    extra = 1


@admin.register(MainBanner)
class IndexAdminForm(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'button_title']
    inlines = [BannersInline]
