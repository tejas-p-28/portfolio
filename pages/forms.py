from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'details']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address'
            }),
            'details': forms.Textarea(attrs={
                'placeholder': 'Tell me about your project...'
            }),
        }

