from django.urls import path 
from .views import LearningspaceCreate, LearningspaceListView, LearningspaceUserListView, LearningspaceUpdateView, LearningspaceDeleteView, LearningspaceDetailView


urlpatterns = [
    path('', LearningspaceListView.as_view(), name='learningspace-list' ),
    path('add/', LearningspaceCreate.as_view(), name='learningspace-add'),
    path('by/<username>/', LearningspaceUserListView.as_view(), name='learningspace-by'),
    path('<slug:slug>', LearningspaceDetailView.as_view(), name='learningspace-detail'),
    path('edit/<int:pk>', LearningspaceUpdateView.as_view(), name = 'learningspace-edit'),
    path('delete/<int:pk>', LearningspaceDeleteView.as_view(), name='learningspace-delete')
]