from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin

from .models import AboutChefs, Chefs


@admin.register(AboutChefs)
class AboutChefsInline(SingletonModelAdmin):
    fields = ['title', 'subtitle']


@admin.register(Chefs)
class Chefs(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'order', 'draft')
    list_filter = ('title',)
    list_editable = ('draft',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = 'Фото'

