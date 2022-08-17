from django.contrib import admin
from django import forms
from solo.admin import SingletonModelAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import About, AboutBanners


class AboutAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


class AboutBannersInline(admin.TabularInline):
    model = AboutBanners
    extra = 1


@admin.register(About)
class AboutBannersInline(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'text', 'video_prew', 'url']
    inlines = [AboutBannersInline]
    form = AboutAdminForm