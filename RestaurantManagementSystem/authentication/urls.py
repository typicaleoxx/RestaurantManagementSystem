from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserDeleteView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
]
