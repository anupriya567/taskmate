from django.shortcuts import render,redirect
from .forms import CustomRegistrationForm
from django.http import HttpResponse
from django.contrib import messages


def register(request):
     if request.method == "POST":
          register_form = CustomRegistrationForm(request.POST)
          if register_form.is_valid():
               register_form.save()
               messages.success(request,("account created successfully! Now login "))
          return redirect('register') 
     else:
          register_form = CustomRegistrationForm()   
     return render(request,'register.html',{'register_form':register_form})
    