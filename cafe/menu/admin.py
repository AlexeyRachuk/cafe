from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Menu, AboutMenu


# CKEditor
class MenuAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Menu
        fields = '__all__'


# Блок меню в админке
@admin.register(AboutMenu)
class AboutMenuInline(SingletonModelAdmin):
    fields = ['title', 'subtitle']


# Компоненты меню в админке
@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_image', 'order', 'draft')
    list_filter = ('name',)
    search_fields = ('name', 'price')
    list_editable = ('draft',)
    form = MenuAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = 'Фото'
