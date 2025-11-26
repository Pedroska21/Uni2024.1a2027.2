from django.contrib import admin
from django.urls import path
from .views import CourseLoginView, Resgister

urlpatterns = [
    path('', CourseLoginView.as_view(), name='login'),
    path ('registrar/', Resgister.as_view(), name='register'),
]