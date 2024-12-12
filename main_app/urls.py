from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('institutions/', views.institution_index, name='institution-index'),
    path('institutions/<int:institution_id>/', views.institution_detail, name='institution-detail'),
    # path('institutions/<int:institution_id>/exhibits/<int:exhibit_id>', views.exhibit_detail, name='exhibit-detail'),
    #path('institutions/create/', views.InstitutionCreate.as_view(), name='institution-create'),
]
