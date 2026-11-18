from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *


def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(username=data['username'], password=data['password'])
        else:
            return redirect("registration")
        return redirect("login")
    return render(request, 'registration.html')    
    

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password']) 
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login')
    return render(request, 'login.html')
    
    
@login_required
def home(request):
    tickets = Tickets.objects.all()
    if request.method == 'GET':
        data = request.GET
        if data.get('departure'):
            tickets = tickets.filter(departure__icontains=data['departure'])
        if data.get('arrival'):
            tickets = tickets.filter(arrival__icontains=data['arrival'])
        if data.get('flight'):
            tickets = tickets.filter(flight=data['flight'])
    return render(request, 'home.html', {'tickets': tickets})


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def create_task(request):
    if request.method == 'POST':
        data = request.POST
        Tickets.objects.create(
            username = request.user,
            airline = Airlines.objects.get(id=data['airline']),
            departure = data['departure'],
            arrival = data['arrival'],
            flight = data['flight'],
            landing = data['landing'],
            price = data['price']
        )
        return redirect("my_tickets")
    return render(request, 'create_ticket.html', {
        'airlines': Airlines.objects.all()
    })


@login_required
def my_tickets(request):
    tickets = Tickets.objects.filter(username=request.user)
    return render(request, 'my_tickets.html', {'tickets': tickets})


@login_required
def edit_ticket(request, id):
    ticket = Tickets.objects.get(id=id, username=request.user)

    if request.method == 'POST':
        data = request.POST
        ticket.airline = Airlines.objects.get(id=data['airline'])
        ticket.departure = data['departure']
        ticket.arrival = data['arrival']
        ticket.flight = data['flight']
        ticket.landing = data['landing']
        ticket.price = data['price']
        ticket.save()

        return redirect("my_tickets")

    return render(request, 'edit_ticket.html', {
        'ticket': ticket,
        'airlines': Airlines.objects.all()
    })
    
    

@login_required
def delete_ticket(request, id):
    ticket = Tickets.objects.get(id=id, username=request.user)

    if request.method == 'POST':
        ticket.delete()
        return redirect("my_tickets")

    return render(request, 'delete_ticket.html', {'ticket': ticket})
