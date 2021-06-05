from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Educator(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    degree = models.CharField(max_length=200, verbose_name='Степень')

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'

    def __str__(self):
        return "%s, %s" % (self.name, self.degree)


class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, default=None, verbose_name='Группа')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return "%s, %s" % (self.name, self.group)


class Diploma(models.Model):
    title = models.CharField(max_length=300, verbose_name='Тема')
    file = models.FileField(upload_to='diplomas', verbose_name='Файл')
    year = models.IntegerField(default=0, verbose_name='Год')
    author = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Автор')
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE, verbose_name='Педагог')

    class Meta:
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return "%s (%s)" % (self.title, self.year)
