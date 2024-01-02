from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def home(request):
    if not 'count' in request.session.keys():
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    return render(request, 'home.html')

def add_2(request):
    request.session['count'] += 1
    return redirect(reverse('home'))

def reset(request):
    request.session['count'] = -1
    return redirect(reverse('home'))