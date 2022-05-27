from django.urls import path
from .views import (
    StoryListView,
    StoryDetailView,
    StoryCreateView,
    StoryUpdateView,
    StoryDeleteView
)

urlpatterns = [
    path('',StoryListView.as_view(), name='home'),
    path('<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
    path('<int:pk>/edit/', StoryUpdateView.as_view(), name='story_edit'),
    path('<int:pk>/delete/', StoryDeleteView.as_view(), name='story_delete'),
    path('new/',StoryCreateView.as_view(), name='story_new'),
]