from django.urls import path 
from .views import *

urlpatterns = [
    path('', LearningspaceListView.as_view(), name='learningspace-list' ),
    path('add/', LearningspaceCreate.as_view(), name='learningspace-add'),
    path('by/<username>/', LearningspaceUserListView.as_view(), name='learningspace-by'),
    path('<slug:slug>', LearningspaceDetailView.as_view(), name='learningspace-detail'),
    path('edit/<int:pk>', LearningspaceUpdateView.as_view(), name = 'learningspace-edit'),
    path('delete/<int:pk>', LearningspaceDeleteView.as_view(), name='learningspace-delete'),
    path('add-comment/<int:pk>', CommentCreateView.as_view(), name='add-comment'),
    path('edit-comment/<int:pk>', CommentUpdateView.as_view(), name='edit-comment'),
    path('like/<int:pk>', LikeView, name='like-learningspace'),
    path('learningspace_search/', search_learningspaces, name='learningspace-search')
]