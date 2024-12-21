from django.urls import path
from Frogadier_blog.apps import FrogadierBlogConfig
from Frogadier_blog.views import (
    PostListView,
    PostDeleteView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
)

app_name = FrogadierBlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path("Frogadier/", PostListView.as_view(), name="posts_list"),
    path(
        "Frogadier/<int:pk>/",
        PostDetailView.as_view(),
        name="posts_detail",
    ),
    path(
        "Frogadier/create", PostCreateView.as_view(), name="posts_create"
    ),
    path(
        "Frogadier/<int:pk>/update",
        PostUpdateView.as_view(),
        name="posts_update",
    ),
    path(
        "Frogadier/<int:pk>/delete",
        PostDeleteView.as_view(),
        name="posts_delete",
    ),
]