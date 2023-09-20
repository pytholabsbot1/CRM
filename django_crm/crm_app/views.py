from django.shortcuts import render, redirect
from .models import Lead, Label, Activity
from .forms import LeadUpdateForm, ActivityForm

from django.core.paginator import Paginator

def dashboard(request):
    lead_list = Lead.objects.all()
    total_leads = lead_list.count()  # Get the total count of leads
    paginator = Paginator(lead_list, 500)  # Show 500 leads per page

    page = request.GET.get('page')
    leads = paginator.get_page(page)

    return render(request, 'dashboard.html', {
        'leads': leads,
        'total_leads': total_leads  # Pass the total count to the template
    })


def lead_detail(request, lead_id):
    lead = Lead.objects.get(id=lead_id)
    activities = Activity.objects.filter(lead=lead)
    edit_mode = False

    if 'edit' in request.GET:
        edit_mode = True

    if request.method == 'POST' and edit_mode:
        form = LeadUpdateForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_detail', lead_id=lead.id)

    form = LeadUpdateForm(instance=lead)
    activity_form = ActivityForm()

    return render(request, 'lead_detail.html', {
        'lead': lead, 
        'activities': activities,
        'form': form,
        'activity_form': activity_form,
        'edit_mode': edit_mode
    })


def add_activity(request, lead_id):
    lead = Lead.objects.get(id=lead_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.lead = lead
            activity.save()
            return redirect('lead_detail', lead_id=lead.id)
    else:
        form = ActivityForm()
    return render(request, 'add_activity.html', {'form': form})
