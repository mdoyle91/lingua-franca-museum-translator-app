from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('exhibits/', views.exhibit_index, name='exhibit-index'),
    # path('institutions/<int:institution_id>/exhibits/<int:exhibit_id>', views.exhibit_detail, name='exhibit-detail'),
    #path('institutions/create/', views.InstitutionCreate.as_view(), name='institution-create'),
]
