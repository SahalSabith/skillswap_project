from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import SkillRequest, Message
from skills.models import Skill
from .forms import SkillRequestForm, MessageForm

class SendRequestView(LoginRequiredMixin, View):
    template_name = 'skill_requests/request_form.html'

    def get(self, request, skill_id):
        skill = get_object_or_404(Skill, id=skill_id)
        if skill.user == request.user:
            messages.error(request, "You cannot request your own skill!")
            return redirect('skills:detail', pk=skill_id)
        
        form = SkillRequestForm()
        return render(request, self.template_name, {'form': form, 'skill': skill})

    def post(self, request, skill_id):
        skill = get_object_or_404(Skill, id=skill_id)
        form = SkillRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.sender = request.user
            req.receiver = skill.user
            req.skill = skill
            req.save()
            messages.success(request, f"Request sent to {skill.user.full_name} for '{skill.name}'")
            return redirect('accounts:dashboard')
        return render(request, self.template_name, {'form': form, 'skill': skill})

class RequestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = SkillRequest
    template_name = 'skill_requests/request_detail.html'
    context_object_name = 'skill_request'

    def test_func(self):
        req = self.get_object()
        return self.request.user == req.sender or self.request.user == req.receiver

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_form'] = MessageForm()
        context['messages_list'] = self.object.messages.all()
        return context

class ReplyView(LoginRequiredMixin, View):
    def post(self, request, pk):
        req = get_object_or_404(SkillRequest, pk=pk)
        if request.user != req.sender and request.user != req.receiver:
            messages.error(request, "Permission denied.")
            return redirect('accounts:dashboard')
        
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.request = req
            msg.sender = request.user
            msg.save()
            messages.success(request, "Message sent!")
        return redirect('skill_requests:detail', pk=pk)

class UpdateStatusView(LoginRequiredMixin, View):
    def post(self, request, pk, status):
        req = get_object_or_404(SkillRequest, pk=pk)
        if request.user != req.receiver:
            messages.error(request, "Permission denied.")
            return redirect('accounts:dashboard')
        
        if status in ['A', 'R']:
            req.status = status
            req.save()
            status_text = "Accepted" if status == 'A' else "Rejected"
            messages.success(request, f"Request {status_text}!")
        
        return redirect('skill_requests:detail', pk=pk)
