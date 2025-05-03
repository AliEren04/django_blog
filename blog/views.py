from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .forms import CommentForm
from .models import Post, Comment
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    posts = Post.objects.filter(active = True)
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def all_posts(request):
     return None

def blog(request, post_id):
        related_post = get_object_or_404(Post, post_id) # When using utility first model then parameter id taken
        if request.method == "POST": 
            form = CommentForm(request.POST)
            if form.is_valid(): 
                name  = form.cleaned_data["name"]
                body = form.cleaned_data["body"]
                Comment.objects.create(post= related_post, name = name, body = body)
                return redirect() #path of html and post id to redirect in that post
        else:
            return CommentForm() 

        



