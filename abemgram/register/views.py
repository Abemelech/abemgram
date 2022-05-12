from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/login")

    else:
        form = RegisterForm()

    return render(response, 'register/register.html', {'form':form})