from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('article/<slug:slug>/', views.fashion_post, name='fashion_post'),
]