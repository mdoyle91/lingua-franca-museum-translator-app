from django import forms
from .models import Exhibit

class ExhibitsForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['name', 'exhibit_number', 'exhibit_image', 'original_language_text', 'english_language_text', 'spanish_language_text', 'portuguese_language_text']