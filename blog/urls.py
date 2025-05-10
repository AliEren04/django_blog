from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]