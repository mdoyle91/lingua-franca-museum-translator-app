from django.shortcuts import render
from .models import Exhibit



# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request): #Will remove this eventually.
    return render(request, 'about.html')

def institution_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'institution/index.html', {'institutions': institutions})

# def exhibit_index(request): 
#     exhibits = Exhibit.objects.all()
#     return render(request, 'exhibits/exhibit-index.html', {'exhibits': exhibits})

#  def exhibit_detail(request):  
#     return render(request, 'exhibits/exhibit-detail.html', {'exhibits': exhibits}) #May need to alter the portin in curly brackets at the end.