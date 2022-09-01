from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Main, MainMenu, Form


class MainAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Main
        fields = '__all__'


class MainMenuInline(admin.TabularInline):
    model = MainMenu
    extra = 1


@admin.register(Main)
class AboutBannersInline(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'text', 'phone_1', 'phone_2', 'email_1', 'email_2', 'instagram', 'copywrite', 'seo_title', 'seo_descr']
    inlines = [MainMenuInline]
    form = MainAdminForm


@admin.register(Form)
class FormContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'person')
