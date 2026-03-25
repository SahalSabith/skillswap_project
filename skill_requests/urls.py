from django.urls import path
from .views import (
    SendRequestView, RequestDetailView, ReplyView, UpdateStatusView
)

app_name = 'skill_requests'

urlpatterns = [
    path('send/<int:skill_id>/', SendRequestView.as_view(), name='send'),
    path('<int:pk>/', RequestDetailView.as_view(), name='detail'),
    path('<int:pk>/reply/', ReplyView.as_view(), name='reply'),
    path('<int:pk>/status/<str:status>/', UpdateStatusView.as_view(), name='update_status'),
]
