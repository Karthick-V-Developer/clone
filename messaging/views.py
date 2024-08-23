from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def chat_view(request, recipient_id):
    recipient = User.objects.get(id=recipient_id)
    if request.method == "POST":
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=request.user, recipient=recipient, content=content)
    messages = Message.objects.filter(sender=request.user, recipient=recipient) | \
              Message.objects.filter(sender=recipient, recipient=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'chat.html', {'recipient': recipient, 'messages': messages})

