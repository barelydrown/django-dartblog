from django.urls import path, include

from .views import (
    CategoryListView, TagListView, PostListView,
    CategoryRetrieveView, TagRetrieveView, PostRetrieveView,

)

urlpatterns = [
    path('auth/', include('djoser.urls')),

    # Category Model
    path('category/all/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveView.as_view()),

    # Tag Model
    path('tag/all/', TagListView.as_view()),
    path('tag/<int:pk>/', TagRetrieveView.as_view()),

    # Post Model
    path('post/all/', PostListView.as_view()),
    path('post/<int:pk>/', PostRetrieveView.as_view()),
]