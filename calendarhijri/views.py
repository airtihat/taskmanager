from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path
from . import views


def dashboard_view(request):
    return render(request, 'calendarhijri/dashboard.html')

@login_required
def hijri_calendar(request):
    return render(request, 'calendarhijri/calendar.html')

@login_required
def calendarhijri_dashboard(request):
    return render(request, 'calendarhijri/dashboard.html')