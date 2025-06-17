from django import forms

from .models import User, LoomVideo
from django.forms import DateTimeField

class LoomVideoForm(forms.ModelForm):
    class Meta:
        model = LoomVideo
        fields = ['title', 'link', 'user', 'transcript', 'summary', 'team', 'tags','created_at']
        field_classes = {
            'created_at':DateTimeField,
        }