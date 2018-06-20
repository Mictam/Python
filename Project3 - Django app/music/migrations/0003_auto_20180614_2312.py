# Generated by Django 2.0.6 on 2018-06-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180614_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='song',
            name='field',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
