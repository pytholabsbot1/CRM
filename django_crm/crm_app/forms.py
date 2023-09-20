from django import forms
from .models import Lead, Activity

class LeadUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['label', 'notes']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'notes']
