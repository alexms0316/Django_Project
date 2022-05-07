from django.urls import path
from users.views import SignupView, LoginView, EmailValidateView
urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/emailvalidation', EmailValidateView.as_view()),
    path('/login',  LoginView.as_view())
]