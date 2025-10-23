from django.shortcuts import render, redirect
from .forms import FeedbackForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

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

def tools_apps(request):
    return render(request, 'tools_apps.html')

def crisis(request):
    return render(request, 'crisis.html')

def crisis_support(request):
    return render(request, 'crisis_support.html')

def content(request):
    return render(request, 'content.html')
