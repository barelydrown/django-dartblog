from django.urls import path, include
from .views import (
    CategoryListView, TagListView, PostListView
)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('category/all/', CategoryListView.as_view()),
    path('tag/all/', TagListView.as_view()),
    path('post/all/', PostListView.as_view()),
]