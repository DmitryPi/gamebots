# Generated by Django 4.0.8 on 2022-11-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0005_alter_bot_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='title_sm',
        ),
        migrations.AddField(
            model_name='bot',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, verbose_name='Subtitle'),
        ),
    ]
