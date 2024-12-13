from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('institutions/', views.institution_index, name='institution-index'),
    path('institutions/<int:institution_id>/', views.institution_detail, name='institution-detail'), #Comment this out if it causes issues.
    path('institutions/create', views.InstitutionCreate.as_view(), name='institution-create'),
    path ('institutions/<int:institution_id>/add-exhibit/', views.add_exhibit, name='add-exhibit'),
    path('institutions/<int:institution_id>/exhibits/<int:pk>/update', views.ExhibitUpdate.as_view(), name='exhibit-update'),
    path('institutions/<int:institution_id>/exhibits/<int:pk>/delete', views.ExhibitDelete.as_view(), name='exhibit-delete'),
]
