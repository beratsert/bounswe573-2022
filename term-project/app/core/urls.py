from django.urls import path 
from .views import WorkspaceCreate, WorkspaceListView, WorkspaceUserListView


urlpatterns = [
    path('', WorkspaceListView.as_view(), name='workspace-list' ),
    path('add/', WorkspaceCreate.as_view(), name='workspace-add'),
    path('by/<username>/', WorkspaceUserListView.as_view(), name='workspace-by'),
]