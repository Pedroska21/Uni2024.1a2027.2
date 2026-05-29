from django.contrib import admin
from django.urls import path
from .views import CreateEpisode, UpdateEpisode, DeleteEpisode

app_name = 'episodios'
urlpatterns = [

    path('inserir/', CreateEpisode.as_view(), name='create-episode'),
    path('<int:pk>/atualizar', UpdateEpisode.as_view(), name='update-episode'),
    path('<int:pk>/remover', DeleteEpisode.as_view(), name='delete-episode'),
]