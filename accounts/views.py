from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Profile
from .forms import CustomUserCreationForm, UserLoginForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import login
from django.contrib import messages
from skill_requests.models import SkillRequest

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        Profile.objects.get_or_create(user=self.object)
        messages.success(self.request, "Account created successfully!")
        return response

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/profile_update.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form})

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile', pk=request.user.pk)
        
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form})

class ProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'

class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'accounts/dashboard.html'
    context_object_name = 'received_requests'

    def get_queryset(self):
        return SkillRequest.objects.filter(receiver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sent_requests'] = SkillRequest.objects.filter(sender=self.request.user)
        return context
