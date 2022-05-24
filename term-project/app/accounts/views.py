from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, EditProfileForm


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