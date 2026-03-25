from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full py-3 px-4 rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full py-3 px-4 rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'block w-full py-3 px-4 rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'block w-full py-3 px-4 rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border',
                'rows': 4,
                'placeholder': 'Message'
            }),
        }
