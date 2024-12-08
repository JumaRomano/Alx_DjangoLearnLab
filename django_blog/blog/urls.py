# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('tags/<str:tag_name>/', views.tagged_posts, name='tagged_posts'),
    path('search/', views.search_posts, name='search_posts'),
]
comment/<int:pk>/update/
post/<int:pk>/comments/new/
comment/<int:pk>/delete/
post/<int:pk>/update/
login/", "register/
profile/