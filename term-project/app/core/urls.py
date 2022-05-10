from django.urls import path 
from .views import WorkspaceCreate, WorkspaceListView


urlpatterns = [
    path('', WorkspaceListView.as_view(), name='workspace-list' ),
    path('add/', WorkspaceCreate.as_view(), name='workspace-add')
]