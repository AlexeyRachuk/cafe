# Generated by Django 4.1 on 2022-09-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_form_date_remove_form_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='seo_descr',
            field=models.CharField(default=1, max_length=255, verbose_name='Seo Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main',
            name='seo_title',
            field=models.CharField(default=1, max_length=100, verbose_name='Seo Title'),
            preserve_default=False,
        ),
    ]
