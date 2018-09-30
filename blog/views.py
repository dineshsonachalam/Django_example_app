from django.shortcuts import render
from .models import Post # Here . means current directory or current application

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
