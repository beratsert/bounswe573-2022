from django.shortcuts import render, get_object_or_404 
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from .models import Learningspace, Comment
from .forms.form import CommentForm


class OwnerProtectMixin(object):
    def dispatch(self, request, *args, **kwargs):
        objectUser = self.get_object()
        if objectUser.user != self.request.user:
            return HttpResponseForbidden()
        return super(OwnerProtectMixin, self).dispatch(request, *args, **kwargs)

class LearningspaceListView(ListView):
    model = Learningspace
    context_object_name = "objLearningspaces"
    queryset = Learningspace.objects.order_by('-created_at')

@method_decorator(login_required, name='dispatch')
class LearningspaceCreate(CreateView):
    model = Learningspace
    fields = ['title','desc']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LearningspaceUserListView(ListView):
    template_name = 'core/learningspace_by_user.html'
    def get_queryset(self):
        self.user = get_object_or_404(User, username = self.kwargs['username'])
        return Learningspace.objects.filter(user = self.user)

class LearningspaceDetailView(DetailView):
    model = Learningspace
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

@method_decorator(login_required, name='dispatch')
class LearningspaceUpdateView(OwnerProtectMixin, UpdateView):
    model = Learningspace
    fields = ['title','desc']
    template_name = 'core/learningspace_update_form.html'

@method_decorator(login_required, name='dispatch')
class LearningspaceDeleteView(OwnerProtectMixin, DeleteView):
    model = Learningspace
    success_url = '/core'

@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    fields = ['desc']

    def form_valid(self, form):
        _learningspace = get_object_or_404(Learningspace, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.slug = _learningspace
        return super().form_valid(form)
    
    success_url = '/core'