from django.shortcuts import render

from django.http import HttpResponse
from .models import LoomVideo, User
from django.views import generic
    
    
def HomeView(request):
    template_name = 'loom/HomeIndex.html'

    return render(request, 'loom/homeIndex.html')




class IndexView(generic.ListView):
    template_name = 'loom/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return LoomVideo.objects.all()



class UserIndexView(generic.ListView):
    template_name = 'loom/userIndex.html'
    context_object_name = 'user_list'
    model = User

    def get_queryset(self):
        return User.objects.all()

class UserVideosView(generic.ListView):
    template_name = 'loom/index.html'
    context_object_name = 'latest_video_list'
    model = User
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return LoomVideo.objects.filter(user = user_id)
