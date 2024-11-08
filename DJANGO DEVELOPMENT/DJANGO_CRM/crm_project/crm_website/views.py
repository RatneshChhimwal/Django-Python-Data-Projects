from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import *
from django.contrib import messages
from .forms import *
from .models import *


# Create your views here.

def home(request):
    # check to see if the user is logging in

    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # AUTHENTICATE

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "YOU HAVE BEEN LOGGED IN")
            return redirect('home')
        else:
            messages.error(request, "ERROR LOGGING IN, TRY AGAIN!!")
            return redirect('home')

    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "YOU HAVE BEEN LOGGED OUT")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered successfully, Welcome!!")
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "YOU ARE NOT LOGGED IN, KINDLY LOG IN!!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        delete_customer = Record.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request, "The record has been successfully deleted")
        return redirect('home')
    else:
        messages.error(request, "YOU ARE NOT LOGGED IN, KINDLY LOG IN!!")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "The record was added successfully")
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "YOU ARE NOT LOGGED IN, KINDLY LOG IN!!")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        else:
            return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "YOU ARE NOT LOGGED IN, KINDLY LOG IN!!")
        return redirect('home')
