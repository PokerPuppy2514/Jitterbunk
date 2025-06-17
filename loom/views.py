from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import LoomVideo, User
from django.views import generic
from .forms import LoomVideoForm
    
    
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

def userVideos(request, user_id):
    video_list = LoomVideo.objects.filter(user__pk = user_id)
    return render(request, 'loom/userVideos.html', {'video_list' : video_list})

def add_video(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoomVideoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoomVideoForm()

    return render(request, 'loom/submit.html', {'form': form})
