# Generated by Django 3.2.3 on 2021-05-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkrapp', '0003_alter_diploma_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diploma',
            name='file',
            field=models.FileField(upload_to='diplomas', verbose_name='Файл'),
        ),
    ]
