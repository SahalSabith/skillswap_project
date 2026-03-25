from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Profile
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=150, 
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabetical characters and spaces allowed.')],
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'w-full px-4 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'w-full px-4 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500'})
    )

    class Meta:
        model = User
        fields = ('email', 'full_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'full_name')

from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-indigo-600 outline-none transition duration-200'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-indigo-600 outline-none transition duration-200'
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'skills_wanted']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'avatar': forms.FileInput(attrs={'class': 'w-full'}),
            'skills_wanted': forms.TextInput(attrs={'placeholder': 'e.g. Photoshop, Guitar', 'class': 'w-full px-4 py-2 border rounded-lg'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'readonly': 'readonly'}),
        }
