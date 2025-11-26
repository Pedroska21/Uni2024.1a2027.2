from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from episodes.models import Episodes

class CreateEpisode(CreateView):
    model = Episodes
    fields = '__all__'
    template_name = 'episodes/create_episode.html'

class UpdateEpisode(UpdateView):
    model = Episodes
    fields = ['Titulo']
    template_name = 'episodes/create_episode.html'

class DeleteEpisode(DeleteView):
    model = Episodes
    template_name = 'episodes/delete_episode.html'
    
    def get_success_url(self):
        return reverse('cursos')
