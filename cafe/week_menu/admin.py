from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import WeekMenu, WeekMenuType, WeekMenuAbout


# CKEditor
class WeekMenuAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = WeekMenu
        fields = '__all__'


# Блок недельного меню в админке
@admin.register(WeekMenuAbout)
class AboutMenuInline(SingletonModelAdmin):
    fields = ['title', 'subtitle']


# Типы недельного меню в админке
@admin.register(WeekMenuType)
class Menu(admin.ModelAdmin):
    list_display = ('title', 'url',)


# Компоненты недельного меню в админке
@admin.register(WeekMenu)
class Menu(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_image', 'breakfast', 'lunch', 'dinner', 'order', 'draft')
    list_filter = ('title',)
    search_fields = ('title', 'price')
    list_editable = ('breakfast', 'lunch', 'dinner', 'draft',)
    form = WeekMenuAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="50"')

    get_image.short_description = 'Фото'
