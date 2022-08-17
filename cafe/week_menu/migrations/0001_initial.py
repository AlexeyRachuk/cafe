# Generated by Django 4.1 on 2022-08-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeekMenuAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок блока')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Заголовок блока')),
            ],
            options={
                'verbose_name': 'Настройки недельного меню',
            },
        ),
        migrations.CreateModel(
            name='WeekMenuType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тип меню')),
                ('url', models.CharField(max_length=50, verbose_name='Ссылка для таба')),
            ],
            options={
                'verbose_name': 'Типы меню для табов',
                'verbose_name_plural': 'Типы меню для табов',
            },
        ),
        migrations.CreateModel(
            name='WeekMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('descr', models.CharField(max_length=255, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='image/', verbose_name='Фото')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Порядок')),
                ('draft', models.BooleanField(default=True, verbose_name='Публикация')),
                ('type', models.ManyToManyField(related_name='type', to='week_menu.weekmenutype', verbose_name='Тип меню')),
            ],
            options={
                'verbose_name': 'Недельное меню',
                'verbose_name_plural': 'Недельное меню',
            },
        ),
    ]