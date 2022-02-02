from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='pf-home'),
    path('about/', views.about, name='pf-about'),
    path('academics/', views.academics, name='pf-academics'),
    path('contact/', views.contact, name='pf-contact'),
    path('blogs/', views.blogs, name='pf-blogs'),
]

urlpatterns+=staticfiles_urlpatterns()
