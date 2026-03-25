from django import forms
from .models import SkillRequest, Message

class SkillRequestForm(forms.ModelForm):
    class Meta:
        model = SkillRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'block w-full p-4 border rounded-xl bg-gray-50 focus:bg-white transition-all outline-none border-gray-200 focus:border-indigo-600 focus:ring-1 focus:ring-indigo-600',
                'rows': 4,
                'placeholder': 'Explain why you are interested in this skill and what you can offer in return!'
            })
        }
    
    def clean_message(self):
        msg = self.cleaned_data.get('message')
        if len(msg) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return msg

class MessageForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'block w-full p-4 border rounded-xl bg-gray-50 focus:bg-white transition-all outline-none border-gray-200 focus:border-indigo-600 focus:ring-1 focus:ring-indigo-600',
            'rows': 2,
            'placeholder': 'Type your message here...'
        }),
        required=True
    )
    class Meta:
        model = Message
        fields = ['content']
