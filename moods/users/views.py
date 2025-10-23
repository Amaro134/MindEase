from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
# ------------------------------
from .models import CustomUser as User  # ensure correct model is imported
User = get_user_model()

# ------------------------------
# Signup


def signup_view(request):
    if request.method == "POST":
        full_name = request.POST.get('fullname', '').strip()  # fixed field name
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Validations
        if not full_name or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('signup')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        # Create user
        user = User.objects.create_user(email=email, password=password, full_name=full_name)
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'signup.html')



# ------------------------------
# Login
# ------------------------------

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # Authenticate using email instead of username
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Welcome, {user.full_name}!")
            return redirect('homePage')  # Your homepage
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')  # Redirect back to login if failed

    return render(request, 'login.html')

# ------------------------------
# Logout
# ------------------------------
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    # Redirect to the logout confirmation page instead of login
    return render(request, 'logout.html')

# ------------------------------
# Password Reset Views
# ------------------------------
ForgotPasswordView = auth_views.PasswordResetView.as_view(
    template_name='forgot_password.html'
)

PasswordResetDoneView = auth_views.PasswordResetDoneView.as_view(
    template_name='password_reset_done.html'
)

PasswordResetConfirmView = auth_views.PasswordResetConfirmView.as_view(
    template_name='password_reset_confirm.html'
)

PasswordResetCompleteView = auth_views.PasswordResetCompleteView.as_view(
    template_name='password_reset_complete.html'
)
