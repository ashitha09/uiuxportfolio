from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/jewelry/', views.jewelry_case_study, name='jewelry_case_study'),
    path('projects/mindspace/', views.mindspace_case_study, name='mindspace_case_study'),
    path('projects/smarthome/', views.smarthome_case_study, name='smarthome_case_study'),
    path('projects/gocab/', views.gocab_case_study, name='gocab_case_study'),

]
