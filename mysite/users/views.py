from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(Request):

    if Request.method == "POST":
        form = UserCreationForm(Request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(Request,f'Welcome {username},your account is successfully created')
            return redirect('index')
    else:
        form=UserCreationForm()
    return render (Request,'users/register.html',{'form':form})
    


