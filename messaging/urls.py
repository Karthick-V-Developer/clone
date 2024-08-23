from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:recipient_id>/', views.chat_view, name='chat_view'),
]
