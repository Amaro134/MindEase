from django import forms
from .models import Feedback, ContactMessage

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Your Feedback'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
