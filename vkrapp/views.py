from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Diploma, Group


def index(request):
    return render(request, 'index.html')


def search(request):
    year = request.GET.get('year', '')
    group = request.GET.get('group', '')
    title = request.GET.get('title', '')
    student = request.GET.get('student', '')
    educator = request.GET.get('educator', '')

    diplomas = Diploma.objects

    if year and year.isnumeric():
        year = int(year)
        diplomas = diplomas.filter(year=year)
    if group and group.isnumeric():
        group = int(group)
        diplomas = diplomas.filter(student__group=group)
    if title:
        slices = title.split()
        for slice in slices:
            diplomas = diplomas.filter(title__icontains=slice)
    if student:
        slices = student.split()
        for slice in slices:
            diplomas = diplomas.filter(student__name__icontains=slice)
    if educator:
        slices = educator.split()
        for slice in slices:
            diplomas = diplomas.filter(educator__name__icontains=slice)

    advanced_shown = True if (year or group or student or educator) else False
    context = {
        'diplomas': diplomas,
        'groups': Group.objects,
        'advanced_shown': advanced_shown,
        'form': {
            'year': year,
            'group': group,
            'title': title,
            'student': student,
            'educator': educator,
        }
    }
    return render(request, 'search.html', context)


def detail(request, diploma_id):
    diploma = get_object_or_404(Diploma, pk=diploma_id)
    return render(request, 'detail.html', {'diploma': diploma})
