from django.shortcuts import render
from .forms import CommentForm
from .models import Post, Comment
from django.contrib import messages

# Create your views here.
def home(request):
    posts = Post.objects.filter(active = True)
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')

def post(request, post_id):
        related_post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=related_post)
        if request.method == "POST": 
            form = CommentForm(request.POST)
            if form.is_valid(): 
                comment = form.save(commit=False)
                comment.post = related_post
                comment.save()
                messages.success(request, "Comment Published Successfully!")

            else:
                 messages.error(request, "Error While Publishing Comment!") 
        else:
            form = CommentForm()
        return render(request, 'blog/blog.html', {'form':form,'post':related_post, 'comments':comments})

        



