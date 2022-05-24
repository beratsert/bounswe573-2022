from django.urls import path

from .views import EditView, SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("edit_profile/", EditView.as_view(), name = "edit_profile")
]