from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('<int:diploma_id>', views.detail, name='detail'),
]
