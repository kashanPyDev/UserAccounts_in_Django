from django.shortcuts import render

# # Create your views here.
# # blog/views.py

# from django.shortcuts import render
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})



# blog/views.py

from django.shortcuts import render, get_object_or_404  # new
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):  # new
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})