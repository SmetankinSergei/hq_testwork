from django.contrib.auth.views import LoginView
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]
