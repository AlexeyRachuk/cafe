# Generated by Django 4.1 on 2022-09-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week_menu', '0004_remove_weekmenu_type_weekmenu_breakfast_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekmenu',
            name='dinner',
            field=models.BooleanField(default=False, verbose_name='Ужин'),
        ),
        migrations.AlterField(
            model_name='weekmenu',
            name='lunch',
            field=models.BooleanField(default=False, verbose_name='Обед'),
        ),
    ]