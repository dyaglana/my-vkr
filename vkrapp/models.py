from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Educator(models.Model):
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)

    def __str__(self):
        return "%s, %s" % (self.name, self.degree)


class Student(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.name, self.group)


class Diploma(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%d)" % (self.title, self.year)
