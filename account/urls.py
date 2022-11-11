from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_views

from .views import password_reset_request


urlpatterns = [
    path('register/', account_views.register, name='account-register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='account-logout'),
    path('profile/', account_views.profile, name='account-profile'),

    path("password_reset/", password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),  


    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
]