from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from team.models import Team

@login_required
def dashboard(request):
    team = request.user.userprofile.get_active_team()

    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')
    clients = Client.objects.filter(team=team).order_by('-created_at')
    rate = round((Client.objects.filter(team=team).count() /Lead.objects.filter(team=team, converted_to_client=False).count()) * 100, 1)
    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
        'rate': rate
    })