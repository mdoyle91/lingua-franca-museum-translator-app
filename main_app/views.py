from django.shortcuts import render
from .models import Exhibit, Institution



# Create your views here.


def home(request):
    return render(request, 'home.html')

def institution_index(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions/index.html', {'institutions': institutions})

# def institution_detail(request): 
#      exhibits = Exhibit.objects.all()
#     return render(request, 'exhibits/index.html', {'exhibits': exhibits})

#  def exhibit_detail(request):  
#     return render(request, 'exhibits/exhibit-detail.html', {'exhibits': exhibits}) #May need to alter the portin in curly brackets at the end.