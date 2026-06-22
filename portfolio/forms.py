from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'interest', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'interest': forms.Select(choices=[
                ('', 'Select service'),
                ('Frontend Development', 'Frontend Development'),
                ('Backend Development', 'Backend Development'),
                ('API Development', 'API Development'),
                ('Full-stack Website', 'Full-stack Website'),
            ]),
            'message': forms.Textarea(attrs={'placeholder': 'Tell me about your project...', 'rows': 5}),
        }
