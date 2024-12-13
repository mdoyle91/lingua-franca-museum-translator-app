from django import from .forms import 
from .models import Exhibits

class ExhibitsForm(forms.ModelForm):
    class Meta:
        model = Exhibits
        fields = []