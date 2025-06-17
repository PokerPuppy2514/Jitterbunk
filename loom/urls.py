"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from . import views


urlpatterns = [
    #chose between unflitered and filtered URL's
    path('', views.home_view, name = 'homeIndex'),
    path('index/', views.IndexView.as_view(), name = 'index'),
    path('users/', views.UserIndexView.as_view(), name='user_index'),
    path('users/<int:user_id>', views.user_videos, name= "user_videos"),
    path('submit/', views.add_video, name='add_video'),
    path('teams/',views.team_view, name = 'team_view'),
    path('teams/<str:team_name>', views.team_videos, name = "team_videos"),
    path('transcript/<int:video_id>', views.transcript, name = 'transcript')
]




# urlpatterns = [
#     path('', views.IndexView.as_view(), name = 'index')
#     path('users/<int:pk>/', views.UserIndexView.as_view(), name='user_index')
# 
