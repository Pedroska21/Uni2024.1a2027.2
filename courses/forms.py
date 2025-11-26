from django.forms import ModelForm
from .models import course


class CourseForm(ModelForm):
    class Meta:
        model = course
        fields = ['name', 'hours', 'description', 'banner', 'category', 'episode']