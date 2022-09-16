from datetime import date

from django.db import models


# Модель формы бронирования
class Form(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.CharField('Email', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    person = models.CharField('Колличество гостей', max_length=50)
    message = models.CharField('Сообщение', max_length=255)

    class Meta:
        verbose_name = "Заявки с формы бронирования"
        verbose_name_plural = "Заявки с формы бронирования"

    def __str__(self):
        return "Заявки с формы бронирования"


# Данные: с баннера, контакты, seo
class Main(models.Model):
    title = models.CharField('Заголовок блока', max_length=50)
    subtitle = models.CharField('Загловок', max_length=100)
    text = models.CharField('Описание', max_length=255)
    phone_1 = models.CharField('Телефон 1', max_length=15)
    phone_2 = models.CharField('Телефон 2', max_length=15)
    email_1 = models.CharField('Email 1', max_length=50)
    email_2 = models.CharField('Email 2', max_length=50)
    instagram = models.URLField('Инстаграм', max_length=100)
    copywrite = models.CharField('Копирайт', max_length=100)
    seo_title = models.CharField('Seo Title', max_length=100)
    seo_descr = models.CharField('Seo Title', max_length=255)

    def __str__(self):
        return "Основные"

    class Meta:
        verbose_name = "Основные"
        verbose_name_plural = "Основные"


# Модель меню
class MainMenu(models.Model):
    title = models.CharField('Пункт меню', max_length=50)
    url = models.CharField('Ссылка меню', max_length=50)
    order = models.SmallIntegerField('Порядок', default=0)
    draft = models.BooleanField('Публикация', default=True)
    id_menu = models.ForeignKey(Main, on_delete=models.CASCADE, related_name='id_menu', default='')

    class Meta:
        verbose_name = "Пункты меню"
        verbose_name_plural = "Пункты меню"
