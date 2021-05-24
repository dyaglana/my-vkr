from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('groups', views.groups, name='groups'),
    path('add', views.add_diploma, name='add_diploma'),
    path('<int:diploma_id>', views.diploma_detail, name='diploma_detail'),
    path('groups/<int:group_id>', views.group_detail, name='group_detail'),
    path('groups/<int:group_id>/<int:student_id>', views.student_detail, name='student_detail'),
]
