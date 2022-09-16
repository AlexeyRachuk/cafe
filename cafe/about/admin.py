from django.contrib import admin
from django import forms
from solo.admin import SingletonModelAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import About, AboutBanners


# Подключение CKEditor
class AboutAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


# Баннеры в слайдере в админке
class AboutBannersInline(admin.TabularInline):
    model = AboutBanners
    extra = 1


# Представление блока «О нас» в админке
@admin.register(About)
class AboutBannersInline(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'text', 'video_prew', 'url']
    inlines = [AboutBannersInline]
    form = AboutAdminForm
