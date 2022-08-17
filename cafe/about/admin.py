from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import About, AboutBanners


class AboutBannersInline(admin.TabularInline):
    model = AboutBanners
    extra = 1


@admin.register(About)
class AboutBannersInline(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'text', 'video_prew', 'url']
    inlines = [AboutBannersInline]