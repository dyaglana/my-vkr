from django.contrib import admin
from .models import Group, Educator, Student, Diploma

admin.site.register([Group, Educator, Student, Diploma])
