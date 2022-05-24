from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class EditView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy("home")
    template_name = "registration/edit_profile.html"

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    template_name='registration/change_password.html'

def password_success(request):
    return render(request, 'registration/password_success.html', {} )