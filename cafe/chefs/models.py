from django.db import models


# Модель блока Шефы
class AboutChefs(models.Model):
    title = models.CharField('Название блока', max_length=50)
    subtitle = models.CharField('Заголовок', max_length=200)

    def __str__(self):
        return "Настройки блока"

    class Meta:
        verbose_name = "Настройки блока"


# Модель шефов
class Chefs(models.Model):
    title = models.CharField('Имя', max_length=100)
    subtitle = models.CharField('Должность', max_length=100)
    descr = models.CharField('Описание', max_length=255)
    photo = models.ImageField('Фото', upload_to='images/')
    instagram = models.URLField('Инстаграм', max_length=100)
    order = models.SmallIntegerField('Порядок', default=0)
    draft = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Шефы"
        verbose_name_plural = "Шефы"
