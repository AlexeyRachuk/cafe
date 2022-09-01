from django.db import models


class WeekMenuAbout(models.Model):
    title = models.CharField('Заголовок блока', max_length=50)
    subtitle = models.CharField('Заголовок блока', max_length=100)

    def __str__(self):
        return "Настройки недельного меню"

    class Meta:
        verbose_name = "Настройки недельного меню"


class WeekMenuType(models.Model):
    title = models.CharField('Тип меню', max_length=50)
    url = models.CharField('Ссылка для таба', max_length=50)
    photo = models.ImageField('Фото', upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Типы меню для табов"
        verbose_name_plural = "Типы меню для табов"


class WeekMenu(models.Model):
    title = models.CharField('Название', max_length=100)
    descr = models.CharField('Описание', max_length=255)
    price = models.IntegerField('Цена')
    photo = models.ImageField('Фото', upload_to='image/')
    breakfast = models.BooleanField('Завтрак', default=False)
    lunch = models.BooleanField('Обед', default=False)
    dinner = models.BooleanField('Ужин', default=False)
    order = models.SmallIntegerField('Порядок', default=0)
    draft = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Недельное меню"
        verbose_name_plural = "Недельное меню"
