from django.contrib import admin
from django.urls import path
from .views import CourseCreateView, CourseDetailView, CourseListView, SearchCourse

urlpatterns = [

    path('inserir', CourseCreateView.as_view(), name='create-course'),
    path('', CourseListView.as_view(), name= 'list-course'),
    path('<int:pk>', CourseDetailView.as_view(), name='detail-course'),
    path('pesquisa/', SearchCourse.as_view(), name='search-course')
]
