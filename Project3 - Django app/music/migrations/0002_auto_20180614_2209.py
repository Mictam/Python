# Generated by Django 2.0.6 on 2018-06-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_file',
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
