from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exhibit, Institution
from .forms import ExhibitsForm



# Create your views here.


def home(request):
    return render(request, 'home.html')

def institution_index(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions/index.html', {'institutions': institutions})

def institution_detail(request, institution_id): 
    institution = Institution.objects.get(id=institution_id)
    exhibits_form= ExhibitsForm()
    return render(request, 'institutions/detail.html', {'institution': institution, 'exhibits_form': exhibits_form})

class InstitutionCreate(CreateView):
    model= Institution
    fields = '__all__'
    success_url= '/institutions/'

def add_exhibit(request, institution_id):
    form = ExhibitForm(request.POST)
    if form.is_valid():
        new_exhibit = form.save(commit=False)
        new_exhibit.institution_id = institution_id
        new_exhibit.save()
    return redirect('institution-detail', institution_id=instituion_id)

class ExhibitUpdate(UpdateView):
    model = Exhibit
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = '__all__'

class ExhibitDelete(DeleteView):
    model = Exhibit
    success_url = '/institutions/'

#  def exhibit_detail(request):  
#     return render(request, 'exhibits/exhibit-detail.html', {'exhibits': exhibits}) #May need to alter the portin in curly brackets at the end.