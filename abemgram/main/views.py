from email import message
from django.shortcuts import render
from .models import Message, Customer
from django.contrib.auth.models import User
from django.db.models import Q

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
        
        search = response.POST.get('search_number')
        chats = Customer.objects.filter(phone = search)

        return render(response, 'main/home.html', {"chats": chats, "search": search, "chat_number": number, 'chat_user': chat_user, 'messages': messages})
    else:
        return render(response, 'main/home.html', {"chat_number": number, 'chat_user': chat_user, 'messages': messages})