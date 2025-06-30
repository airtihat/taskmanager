from django.shortcuts import render

def management_dashboard(request):
    return render(request, 'management/dashboard.html')

def dashboard_view(request):
    return render(request, 'management/dashboard.html')

def team_list(request):
    return render(request, 'management/team_list.html')

def settings_view(request):
    return render(request, 'management/settings.html')
