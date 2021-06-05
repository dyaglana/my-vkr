from django.forms import ModelForm
from .models import Diploma


class DiplomaForm(ModelForm):
    class Meta:
        model = Diploma
        fields = ['title', 'file', 'year', 'author', 'educator']
