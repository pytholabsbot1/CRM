from django.shortcuts import render, redirect
from .models import Lead, Activity, ActivityName, ClientIP
from .forms import ActivityForm, ClientIPForm , LeadUpdateForm
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt


def dashboard(request):
    lead_list = Lead.objects.all().order_by('date')
    total_leads = lead_list.count()
    client_ip, created = ClientIP.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = ClientIPForm(request.POST, instance=client_ip)
        if form.is_valid():
            form.save()

    form = ClientIPForm(instance=client_ip)

    return render(request, 'dashboard.html', {
        'leads': lead_list,
        'total_leads': total_leads,
        'ip_form': form,
        "client_ip" :client_ip
    })



def lead_detail(request, lead_id):
    lead = Lead.objects.get(id=lead_id)
    activities = Activity.objects.filter(lead=lead).order_by('-date_time')
    edit_mode = False

    if 'edit' in request.GET:
        edit_mode = True

    if request.method == 'POST' and edit_mode:
        form = LeadUpdateForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_detail', lead_id=lead.id)

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.lead = lead
            activity.save()

            if activity.name.name == 'SMS':
                client_ip = ClientIP.objects.first().ip_address
                notes_ = activity.notes
                if(notes_.upper()=="INFO"):
                    notes_ = 'Greetings from Airport Enclave Jharsuguda.\n We called you regarding your enquiry for 1/2/3/4 BHK Flats & Duplex Villas. If you have a moment, please give us a call back at 8249544034.'

                response = requests.post(
                    f'http://{client_ip}:5000/sms',
                    json={"number": lead.mobile, "message": notes_}
                )


            if activity.name.name == 'Whatsapp':
                    # Make the POST request

                    num_ = activity.notes.split("|")[0].strip()
                    notes_ = activity.notes.split("|")[1].strip()
                    response = requests.post(
                        'http://0.0.0.0:5000/msg',
                        json={"number": num_, "message": notes_}
                    )
        
        else:
            print(form.errors)

    form = LeadUpdateForm(instance=lead)
    activity_form = ActivityForm()

    return render(request, 'lead_detail.html', {
        'lead': lead, 
        'activities': activities,
        'form': form,
        'activity_form': activity_form,
        'edit_mode': edit_mode
    })


@csrf_exempt
def add_call_activity(request, lead_id):
    if request.method == 'POST':
        lead = Lead.objects.get(id=lead_id)  
        activity_name = ActivityName.objects.get_or_create(name='Call')[0]
        Activity.objects.create(name=activity_name, notes='Call made using client app', lead=lead)
        return JsonResponse({"message": "Call activity added successfully!"}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=400)
