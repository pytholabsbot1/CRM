from django.shortcuts import render
from .models import Lead, Label, Activity

def dashboard(request):
    leads = Lead.objects.all()
    return render(request, 'dashboard.html', {'leads': leads})

def lead_detail(request, lead_id):
    lead = Lead.objects.get(id=lead_id)
    activities = Activity.objects.filter(lead=lead)
    return render(request, 'lead_detail.html', {'lead': lead, 'activities': activities})
