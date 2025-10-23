from django import forms
from .models import MoodEntry

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'note']
        widgets = {
            'mood': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-teal-300 focus:outline-none focus:ring-2 focus:ring-teal-500'
            }),
            'note': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-teal-300 focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Add a note (optional)'
            }),
        }
