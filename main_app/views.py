from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Exhibit, Institution



# Create your views here.


def home(request):
    return render(request, 'home.html')

def institution_index(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions/index.html', {'institutions': institutions})

def institution_detail(request, institution_id): 
    institution = Institution.get(id=institution_id)
    return render(request, 'institutions/index.html', {'institutions': institutions})

class InstitutionCreate(CreateView):
    model= Institution
    fields = '__all__'
    success_url= '/institutions/'

#  def exhibit_detail(request):  
#     return render(request, 'exhibits/exhibit-detail.html', {'exhibits': exhibits}) #May need to alter the portin in curly brackets at the end.