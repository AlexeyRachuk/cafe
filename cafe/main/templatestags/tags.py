from django import template

from slider.models import MainBanner, Banners
from about.models import About, AboutBanners
from menu.models import AboutMenu, Menu
from chefs.models import AboutChefs, Chefs
from main.models import MainMenu
from week_menu.models import WeekMenuAbout, WeekMenu

register = template.Library()


# Тег слайдера
@register.inclusion_tag('tags/main_banner.html')
def get_main_slider():
    main_banner = MainBanner.objects.all()
    return {'main_banners': main_banner}


# Тег баннеров слайдера
@register.inclusion_tag('tags/main_banner_slider.html')
def get_image_sider():
    banner = Banners.objects.all().order_by('order')
    return {'banners': banner}


# Тег блока «О нас»
@register.inclusion_tag('tags/about.html')
def get_about():
    about = About.objects.all()
    return {'abouts': about}


# Тег баннера в блоке «О нас»
@register.inclusion_tag('tags/about_photo.html')
def get_about_photo():
    about_photo = AboutBanners.objects.all().order_by('order')
    return {'about_photos': about_photo}


# Тег меню
@register.inclusion_tag('tags/menu.html')
def get_menu():
    menu = AboutMenu.objects.all()
    return {'menus': menu}


# Тег компонентов меню
@register.inclusion_tag('tags/menu_item.html')
def get_menu_item():
    menu_item = Menu.objects.all().filter(draft=True).order_by('order')
    return {'menu_items': menu_item}


# Тег шефов
@register.inclusion_tag('tags/chefs.html')
def get_chefs():
    about_chef = AboutChefs.objects.all()
    return {'about_chefs': about_chef}


# Тег детальной шефов
@register.inclusion_tag('tags/chefs_item.html')
def get_chefs_item():
    chefs_item = Chefs.objects.all().filter(draft=True).order_by('order')
    return {'chefs_items': chefs_item}


# Тег главного меню
@register.inclusion_tag('tags/main_menu.html')
def get_main_menu():
    main_menu = MainMenu.objects.all().filter(draft=True).order_by('order')
    return {'main_menus': main_menu}


# Тег недельного меню
@register.inclusion_tag('tags/week_menu.html')
def get_week_menu():
    week_menu = WeekMenuAbout.objects.all()
    return {'week_menus': week_menu}


# Тег детальной недельного меню
@register.inclusion_tag('tags/week_menu_item.html')
def get_week_menu_items():
    week_menu_item = WeekMenu.objects.all().filter(draft=True).order_by('order')
    return {'week_menu_items': week_menu_item}


# Тег меню завтраков
@register.inclusion_tag('tags/week_menu_item_breakfast.html')
def get_week_menu_items_breakfast():
    week_menu_item_breakfast = WeekMenu.objects.all().filter(draft=True, breakfast=True).order_by('order')
    return {'week_menu_items_breakfast': week_menu_item_breakfast}


# Тег меню обедов
@register.inclusion_tag('tags/week_menu_item_lunch.html')
def get_week_menu_items_lunch():
    week_menu_item_lunch = WeekMenu.objects.all().filter(draft=True, lunch=True).order_by('order')
    return {'week_menu_items_lunch': week_menu_item_lunch}


# Тег меню ужина
@register.inclusion_tag('tags/week_menu_item_dinner.html')
def get_week_menu_items_dinner():
    week_menu_item_dinner = WeekMenu.objects.all().filter(draft=True, dinner=True).order_by('order')
    return {'week_menu_items_dinner': week_menu_item_dinner}
