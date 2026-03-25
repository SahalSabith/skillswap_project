from django.urls import path
from .views import (
    SkillListView, SkillDetailView, SkillCreateView, 
    SkillUpdateView, SkillDeleteView
)

app_name = 'skills'

urlpatterns = [
    path('', SkillListView.as_view(), name='list'),
    path('create/', SkillCreateView.as_view(), name='create'),
    path('<int:pk>/', SkillDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', SkillUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SkillDeleteView.as_view(), name='delete'),
]
