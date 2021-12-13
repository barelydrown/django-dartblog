from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from .views import (
    CategoryListView, TagListView, PostListView,
    CategoryRetrieveView, TagRetrieveView, PostRetrieveView,
    CategoryCreateView, TagCreateView, PostCreateView,
    CategoryUpdateView, TagUpdateView, PostUpdateView,
    CategoryDestroyView, TagDestroyView, PostDestroyView
)

urlpatterns = [
    # Auth
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refersh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Category Model
    path('category/all/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveView.as_view()),
    path('category/new/', CategoryCreateView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDestroyView.as_view()),

    # Tag Model
    path('tag/all/', TagListView.as_view()),
    path('tag/<int:pk>/', TagRetrieveView.as_view()),
    path('tag/new/', TagCreateView.as_view()),
    path('tag/update/<int:pk>/', TagUpdateView.as_view()),
    path('tag/delete/<int:pk>/', TagDestroyView.as_view()),

    # Post Model
    path('post/all/', PostListView.as_view()),
    path('post/<int:pk>/', PostRetrieveView.as_view()),
    path('post/new/', PostCreateView.as_view()),
    path('post/update/<int:pk>/', PostUpdateView.as_view()),
    path('post/delete/<int:pk>/', PostDestroyView.as_view()),
]