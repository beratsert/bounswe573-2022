from django.shortcuts import render, get_object_or_404 
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from .models import Workspace

@method_decorator(login_required, name='dispatch')

class WorkspaceListView(ListView):
    model = Workspace
    context_object_name = "objWorkspaces"
    queryset = Workspace.objects.all()

class WorkspaceCreate(CreateView):
    model = Workspace
    fields = ['title','desc']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WorkspaceUserListView(ListView):
    template_name = 'core/workspace_by_user.html'
    def get_queryset(self):
        self.user = get_object_or_404(User, username = self.kwargs['username'])
        return Workspace.objects.filter(user = self.user)