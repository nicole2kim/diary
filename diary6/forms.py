from django import forms
from .models import Diary6

class Diaryform(forms.ModelForm):
    class Meta:
        model = Diary6
        fields = ['title', 'body', 'image']
    