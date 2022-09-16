from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from solo.admin import SingletonModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import AboutChefs, Chefs


# CKEditor
class ChefsAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Chefs
        fields = '__all__'


# Данные блока шефов в админке
@admin.register(AboutChefs)
class AboutChefsInline(SingletonModelAdmin):
    fields = ['title', 'subtitle']


# Шефы в админке
@admin.register(Chefs)
class Chefs(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'order', 'draft')
    list_filter = ('title',)
    list_editable = ('draft',)
    form = ChefsAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = 'Фото'
