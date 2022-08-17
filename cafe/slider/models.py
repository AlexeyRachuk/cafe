from django.db import models


class MainBanner(models.Model):
    title = models.CharField('Заголовок баннера', max_length=50)
    subtitle = models.CharField('Подзаголвок баннера', max_length=100)
    button_title = models.CharField('Текст кнопки', max_length=50)


    def __str__(self):
        return "Слайдер"

    class Meta:
        verbose_name = "Слайдер"


class Banners(models.Model):
    photo = models.ImageField('Фото баннера', upload_to="review/", null=True)
    order = models.SmallIntegerField('Порядок', default=0)
    id_photo = models.ForeignKey(MainBanner, on_delete=models.CASCADE, related_name='id_photo', default='')

    class Meta:
        verbose_name = "Изображения баннера"
        verbose_name_plural = "Изображения баннера"
