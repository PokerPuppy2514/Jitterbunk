from django.shortcuts import render

from django.http import HttpResponse
from .models import LoomVideo
from django.views import generic
    
    
class IndexView(generic.ListView):
    template_name = 'loom/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return LoomVideo.objects.all()