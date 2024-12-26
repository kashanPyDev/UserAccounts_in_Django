from django.shortcuts import render

# # Create your views here.
# # blog/views.py

# from django.shortcuts import render
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})



# blog/views.py

# from django.shortcuts import render, get_object_or_404  # new
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

# def post_detail(request, pk):  # new
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "post_detail.html", {"post": post})


# # blog/views.py
# from django.views.generic import ListView, DetailView
# from .models import Post

# class BlogListView(ListView):
#     model = Post
#     template_name = "home.html"

# class BlogDetailView(ListView):
#     model = Post
#     template_name = "home.html"
#     context_object_name = 'posts'



# # blog/views.py
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView
# from .models import Post

# class BlogListView(ListView):
#     model = Post
#     template_name = "home.html"

# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "post_detail.html"

# class BlogCreateView(CreateView):
#     model = Post
#     template_name = "post_new.html"
#     fields = ["title", "author", "body"]

# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")