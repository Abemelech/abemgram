from email import message
import imp
from django.shortcuts import render
from psycopg2 import Timestamp
from .models import Message, Customer
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone

# Create your views here.
def index(response):
    # No Chat selected
    if response.method == "POST":
        
        search = response.POST.get('search_number')
        chats = Customer.objects.filter(phone = search)

        return render(response, 'main/home.html', {"chats": chats, "search": search})
    else:
        return render(response, 'main/home.html', {})

def chat(response, number):
    # If chat has been selected a specific number
    username = Customer.objects.get(phone = number).user
    chat_user = User.objects.get(username = username)

    messages = Message.objects.filter(Q(user=response.user) | Q(user=chat_user), Q(sent_to=response.user) | Q(sent_to=chat_user)).order_by("timestamp")

    # Similar Search function in index
    if response.method == "POST":
        print(response.POST)
        
        search = response.POST.get('search_number')
        chats = Customer.objects.filter(phone = search)
        if response.POST.get("message_box"):
            message_text = response.POST.get("message_box")
            _message = Message.objects.create(user=response.user, sent_to=chat_user, message_text= message_text, timestamp = timezone.now())
            _message.save()

        return render(response, 'main/home.html', {"chats": chats, "search": search, "chat_number": number, 'chat_user': chat_user, 'messages': messages})
    else:
        return render(response, 'main/home.html', {"chat_number": number, 'chat_user': chat_user, 'messages': messages})