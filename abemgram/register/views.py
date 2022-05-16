from django.shortcuts import redirect, render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from main.models import Customer

# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreateForm(response.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user1 = User.objects.get(username=user.username)

            Customer.objects.create(user=user1, phone=user.phone)
            # user1.customer.phone = user.phone
            # user1.save()
            return redirect("/login")

    else:
        form = UserCreateForm()

    return render(response, 'register/register.html', {'form':form})