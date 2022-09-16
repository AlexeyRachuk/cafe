from django.db import models


# Модель блока «Меню»
class AboutMenu(models.Model):
    title = models.CharField('Название блока', max_length=50)
    subtitle = models.CharField('Заголовок', max_length=50)

    def __str__(self):
        return "Настройки меню"

    class Meta:
        verbose_name = "Настройки меню"


# Модель компонентов меню
class Menu(models.Model):
    name = models.CharField('Название блюда', max_length=70)
    descr = models.CharField('Описание блюда', max_length=255)
    price = models.IntegerField('Цена')
    photo = models.ImageField('Фото', upload_to='images/')
    order = models.SmallIntegerField('Порядок', default=0)
    draft = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
