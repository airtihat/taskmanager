from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def events_dashboard(request):
    return render(request, 'family_events/dashboard.html')

@login_required
def event_list(request):
    return render(request, 'family_events/event_list.html')
