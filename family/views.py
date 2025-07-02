from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'family/dashboard.html')

@login_required

def family_dashboard(request):
    return render(request, 'family/dashboard.html')

@login_required
def dashboard_view(request):
    return render(request, 'family/dashboard.html')