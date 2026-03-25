from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from skills.models import Skill, Category

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Random pick for home page? Or just latest.
        context['latest_skills'] = Skill.objects.all().order_by('-created_at')[:3]
        context['categories'] = Category.objects.all()[:6]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(CreateView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your message has been sent. We'll get back to you soon!")
        return response
