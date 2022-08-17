from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin

from .models import Menu, AboutMenu


@admin.register(AboutMenu)
class AboutMenuInline(SingletonModelAdmin):
    fields = ['title', 'subtitle']


@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_image', 'order', 'draft')
    list_filter = ('name',)
    search_fields = ('name', 'price')
    list_editable = ('draft',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = 'Фото'
