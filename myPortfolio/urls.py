from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pf-home'),
    path('about/', views.about, name='pf-about'),
    path('academics/', views.academics, name='pf-academics'),
    path('contact/', views.contact, name='pf-contact'),
]
