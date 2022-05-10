from django.shortcuts import render 
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator

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