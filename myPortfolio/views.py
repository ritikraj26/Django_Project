from django.shortcuts import render
from .models import Post

posts=[
    {
        'author':'Ritik',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted': 'Jan 31, 2022'
    }
]

def home(request):
    return render(request, 'myPortfolio/home.html')
def about(request):
    return render(request, 'myPortfolio/about.html')
def academics(request):
    return render(request, 'myPortfolio/academics.html')
def contact(request):
    return render(request, 'myPortfolio/contact.html')
def blogs(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'myPortfolio/blogs.html', context)
