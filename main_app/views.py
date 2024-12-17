from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exhibit, Institution
from .forms import ExhibitsForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'

def institution_index(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions/index.html', {'institutions': institutions})

def institution_detail(request, institution_id): 
    institution = Institution.objects.get(id=institution_id)
    exhibits_form= ExhibitsForm()
    return render(request, 'institutions/detail.html', {'institution': institution, 'exhibits_form': exhibits_form})

class InstitutionCreate(LoginRequiredMixin, CreateView):
    model= Institution
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

@login_required
def add_exhibit(request, institution_id):
    form = ExhibitsForm(request.POST)
    if form.is_valid():
        new_exhibit = form.save(commit=False)
        new_exhibit.institution_id = institution_id
        new_exhibit.save()
        return redirect('institution-detail', institution_id=institution_id)

class ExhibitUpdate(LoginRequiredMixin, UpdateView):
    model = Exhibit
    fields = '__all__'
    success_url = '/institutions/'

class ExhibitDelete(LoginRequiredMixin, DeleteView):
    model = Exhibit
    success_url = '/institutions/'

