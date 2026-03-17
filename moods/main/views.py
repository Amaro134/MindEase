from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import FeedbackForm, ContactForm
from .models import ContactMessage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out. We'll get back to you soon.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def resources(request):
    return render(request, 'resources.html')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')  # redirect to a thank you page
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_thanks(request):
    return render(request, 'feedback_thanks.html')


def _is_staff(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(_is_staff)
def contact_messages(request):
    messages_qs = ContactMessage.objects.order_by("-submitted_at")
    return render(request, "contact_messages.html", {"messages": messages_qs})

def tools_apps(request):
    return render(request, 'tools_apps.html')

def crisis(request):
    return render(request, 'crisis.html')

def crisis_support(request):
    return render(request, 'crisis_support.html')

def content(request):
    return render(request, 'content.html')
