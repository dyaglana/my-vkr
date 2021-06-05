# Generated by Django 3.2.3 on 2021-05-24 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('degree', models.CharField(max_length=200, verbose_name='Степень')),
            ],
            options={
                'verbose_name': 'Педагог',
                'verbose_name_plural': 'Педагоги',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vkrapp.group', verbose_name='Группа')),
            ],
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Тема')),
                ('file', models.FileField(upload_to='diplomas', verbose_name='Файл')),
                ('year', models.IntegerField(default=0, verbose_name='Год')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkrapp.educator', verbose_name='Педагог')),
            ],
            options={
                'verbose_name': 'Диплом',
                'verbose_name_plural': 'Дипломы',
                'permissions': [('change_own_diploma', 'Can change own diploma'), ('delete_own_diploma', 'Can delete own diploma'), ('view_own_diploma', 'Can view own diploma')],
            },
        ),
    ]
