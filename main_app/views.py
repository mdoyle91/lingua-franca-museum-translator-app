from django.shortcuts import render



# Create your views here.

# main_app/views.py

def home(request):
    # Send a simple HTML response
    return render(request, '<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')
