from django.shortcuts import render,redirect
from .forms import CustomForm
from django.contrib import messages

#we take data as POST requests into our custom made form to register the user and save in the database

def register(request):
    if request.method == "POST":
        register_form = CustomForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Created, You may login"))
            return redirect('register')

    else:
        register_form = CustomForm()
    return render(request, 'users_app/register.html',{'register_form':register_form})