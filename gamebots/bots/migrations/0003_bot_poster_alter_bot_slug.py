# Generated by Django 4.0.8 on 2022-11-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_feature_status_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='poster',
            field=models.ImageField(blank=True, default='', upload_to='posters/', verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='slug',
            field=models.SlugField(blank=True, max_length=55, unique=True, verbose_name='Slug'),
        ),
    ]
