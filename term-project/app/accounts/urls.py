from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EditView, SignUpView, PasswordsChangeView, password_success
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("edit_profile/", EditView.as_view(), name = "edit-profile"),
    #path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/', PasswordsChangeView.as_view(), name = "change-password"),
    path('password_success', views.password_success, name = "password_success")
]