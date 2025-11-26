from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Q
from .models import Course
from .forms import CourseForm

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course-form.html'
    success_url = '<int:pk>/'

class CourseDetailView(DetailView):
    model = Course

    template_name = 'courses/course-detail.html'


class CourseListView(ListView):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        return render(request, 'courses/course-list.html',{ 'courses': courses
})
       
class SearchCourse(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        query_list = Course.objects.filter(
            Q(nome_icontains=query) |
            Q(descricao_icontains=query)
        )

        context = {
            'query_list': query_list
        }

        return render(request, 'courses/course-search.html', context)