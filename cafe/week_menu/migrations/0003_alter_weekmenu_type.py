# Generated by Django 4.1 on 2022-08-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week_menu', '0002_weekmenutype_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekmenu',
            name='type',
            field=models.ManyToManyField(related_name='type_id', to='week_menu.weekmenutype', verbose_name='Тип меню'),
        ),
    ]
