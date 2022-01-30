from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'myPortfolio/home.html')
def about(request):
    return render(request, 'myPortfolio/about.html')
def academics(request):
    return render(request, 'myPortfolio/academics.html')
def contact(request):
    return render(request, 'myPortfolio/contact.html')
