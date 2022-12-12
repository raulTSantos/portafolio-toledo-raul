from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import RegisterView

# Segun el documento de django la url correact para que funcion debe ser accounts/login/
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout')
]