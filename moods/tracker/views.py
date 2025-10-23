from django.shortcuts import render, redirect
from .forms import MoodEntryForm
from .models import MoodEntry
from django.contrib.auth.decorators import login_required
from django.db.models import Count



# Create your views here.
# main/views.py
def mood_tracker(request):
    return render(request, 'main/mood_tracker.html')

from django.shortcuts import render, redirect
from .models import MoodEntry
from .forms import MoodEntryForm
from django.contrib.auth.decorators import login_required

# @login_required
@login_required
def log_mood_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # fallback

    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('dashboard')
    else:
        form = MoodEntryForm()

    mood_entries = MoodEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'log_mood.html', {'form': form, 'mood_entries': mood_entries})


@login_required
def dashboard(request):
    # All entries of the logged-in user
    entries = MoodEntry.objects.filter(user=request.user).order_by('-created_at')
    
    # Most recent entry
    latest_mood = entries.first() if entries.exists() else None
    
    # Total number of entries
    total_entries = entries.count()
    
    # Most frequent mood
    frequent_mood_data = (
        entries.values('mood')
        .annotate(count=Count('mood'))
        .order_by('-count')
        .first()
    )
    frequent_mood = frequent_mood_data['mood'] if frequent_mood_data else None
    
    # Recent entries (last 5)
    recent_entries = entries[:5]
    
    # Pass current year for footer
    import datetime
    year = datetime.datetime.now().year
    
    context = {
        'latest_mood': latest_mood,
        'total_entries': total_entries,
        'frequent_mood': frequent_mood,
        'recent_entries': recent_entries,
        'year': year,
    }
    
    return render(request, 'dashboard.html', context)

