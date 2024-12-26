# # blog/urls.py

# from django.urls import path
# from .views import post_list

# urlpatterns = [
#     path("", post_list, name="home"),
# ]

# # blog/urls.py

# from django.urls import path
# from .views import post_list, post_detail  # new

# urlpatterns = [
#     path("post/<int:pk>/", post_detail, name="post_detail"),  # new
#     path("", post_list, name="home"),
# ]


# # blog/urls.py
# from django.urls import path
# from .views import BlogListView, BlogDetailView

# urlpatterns = [
#     path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
#     path("", BlogListView.as_view(), name="home"),
# ]

# blog/urls.py
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,

)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home"),
]