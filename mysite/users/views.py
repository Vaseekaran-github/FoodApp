from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def register(Request):

    if Request.method == "POST":
        form = RegisterForm(Request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(Request,f'Welcome {username},your account is successfully created')
            return redirect('login')
    else:
        form=RegisterForm()
    return render (Request,'users/register.html',{'form':form})
    


