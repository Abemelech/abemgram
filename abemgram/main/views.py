from django.shortcuts import render
from .models import Message, Customer
from django.contrib.auth.models import User

# Create your views here.
def index(response):
    if response.method == "POST":
        
        search = response.POST.get('search_number')
        users = Customer.objects.filter(phone = search)

        return render(response, 'main/home.html', {"users": users, "search": search})
    else:
        return render(response, 'main/home.html', {})

    