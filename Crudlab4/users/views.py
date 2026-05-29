from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import CreateView

class CourseLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    def get_success_url(self) -> str:
        return reverse_lazy('cursos:list-course')
   
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, "usuario ou senha inválidos")
        return super().form_invalid(form)

class Resgister (CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

def logout_user(request):
    logout(request)
    return redirect  ('cursos')