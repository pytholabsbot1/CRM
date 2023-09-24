from django import forms
from .models import Lead, Activity,ClientIP


class ClientIPForm(forms.ModelForm):
    class Meta:
        model = ClientIP
        fields = ['ip_address']

class LeadUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['label', 'notes']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        schedule = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
        fields = ['name', 'schedule','notes']
