from django import forms

from .models import User, LoomVideo

class LoomVideoForm(forms.ModelForm):
    class Meta:
        model = LoomVideo
        fields = ['title', 'link', 'user', 'transcript', 'summary', 'team', 'tags', 'created_at']