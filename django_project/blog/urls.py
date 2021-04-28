from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Blog-Home'),
    path('about/', views.about, name='Blog-About')
]