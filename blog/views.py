from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')