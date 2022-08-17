from django.db import models


class About(models.Model):
    title = models.CharField('Название блока', max_length=50)
    subtitle = models.CharField('Заголовок блока', max_length=50)
    text = models.CharField('Описание', max_length=255)
    video_prew = models.ImageField('Фото превью видео', upload_to="image/")
    url = models.CharField('Ссылка на видео', max_length=255)

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = "О нас"


class AboutBanners(models.Model):
    photo = models.ImageField('Фото блока', upload_to="image/", null=True)
    order = models.SmallIntegerField('Порядок', default=0)
    id_photo = models.ForeignKey(About, on_delete=models.CASCADE, related_name='id_photo', default='')

    class Meta:
        verbose_name = "Фото блока"
        verbose_name_plural = "Фото блока"
