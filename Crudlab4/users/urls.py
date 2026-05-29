from django.contrib import admin
from django.urls import path
from .views import CourseLoginView, Resgister, logout_user

urlpatterns = [
    path('', CourseLoginView.as_view(), name='login'),
    path ('registrar/', Resgister.as_view(), name='register'),
    path('logout', logout_user, name='logout')
]