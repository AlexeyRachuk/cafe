from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Main, MainMenu, Form


class MainMenuInline(admin.TabularInline):
    model = MainMenu
    extra = 1


@admin.register(Main)
class AboutBannersInline(SingletonModelAdmin):
    fields = ['title', 'subtitle', 'text', 'phone_1', 'phone_2', 'email_1', 'email_2', 'instagram', 'copywrite']
    inlines = [MainMenuInline]


@admin.register(Form)
class FormContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'person')
