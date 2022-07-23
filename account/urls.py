from django.urls import path
from account import views as account_views

urlpatterns = [
    path('register/', account_views.register, name='account-register'),
]