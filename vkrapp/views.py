from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Diploma, Group, Student, Educator
from .forms import DiplomaForm


def index(request):
    return render(request, 'index.html')


def search(request):
    year = request.GET.get('year', '')
    group = request.GET.get('group', '')
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    educator = request.GET.get('educator', '')

    diplomas = Diploma.objects

    if year and year.isnumeric():
        year = int(year)
        diplomas = diplomas.filter(year=year)
    if group and group.isnumeric():
        group = int(group)
        diplomas = diplomas.filter(author__group=group)
    if title:
        slices = title.split()
        for slice in slices:
            diplomas = diplomas.filter(title__icontains=slice)
    if author:
        slices = author.split()
        for slice in slices:
            diplomas = diplomas.filter(author__name__icontains=slice)
    if educator:
        slices = educator.split()
        for slice in slices:
            diplomas = diplomas.filter(educator__name__icontains=slice)

    advanced_shown = True if (year or group or author or educator) else False
    context = {
        'diplomas': diplomas,
        'groups': Group.objects,
        'advanced_shown': advanced_shown,
        'form': {
            'year': year,
            'group': group,
            'title': title,
            'author': author,
            'educator': educator,
        }
    }
    return render(request, 'search.html', context)


def add_diploma(request):
    form = DiplomaForm()
    if request.method == 'POST':
        form = DiplomaForm(request.POST, request.FILES)
        if form.is_valid():
            diploma = form.save()
            return redirect('diploma_detail', diploma_id=diploma.id)

    context = {
        'students': Student.objects.order_by('name'),
        'educators': Educator.objects.order_by('name'),
        'form': form
    }
    return render(request, 'add_diploma.html', context)


def diploma_detail(request, diploma_id):
    diploma = get_object_or_404(Diploma, pk=diploma_id)
    return render(request, 'diploma_detail.html', {'diploma': diploma})


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'group_detail.html', {'group': group})


def student_detail(request, group_id, student_id):
    group = get_object_or_404(Group, pk=group_id)
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student_detail.html', {'group': group, 'student': student})


def groups(request):
    return render(request, 'groups.html', {'groups': Group.objects})
