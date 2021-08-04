from django import forms
from .models import  *

class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['ngo_name','project_name','description','amount']