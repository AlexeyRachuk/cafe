from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import WeekMenu, WeekMenuType, WeekMenuAbout


class WeekMenuAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = WeekMenu
        fields = '__all__'


@admin.register(WeekMenuAbout)
class AboutMenuInline(SingletonModelAdmin):
    fields = ['title', 'subtitle']


@admin.register(WeekMenuType)
class Menu(admin.ModelAdmin):
    list_display = ('title', 'url',)


@admin.register(WeekMenu)
class Menu(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_image', 'order', 'draft')
    list_filter = ('title',)
    search_fields = ('title', 'price')
    list_editable = ('draft',)
    form = WeekMenuAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="50"')

    get_image.short_description = 'Фото'
