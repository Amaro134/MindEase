from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Password reset URLs
    path('forgot-password/', views.ForgotPasswordView, name='forgot_password'),
    path('password-reset-done/', views.PasswordResetDoneView, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView, name='password_reset_confirm'),
    path('reset-complete/', views.PasswordResetCompleteView, name='password_reset_complete'),
]
