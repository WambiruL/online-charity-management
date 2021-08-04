from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def viewDonationRequest(request):
    requests = DonationRequest.objects.all()
    context={'requests':requests}
    return render(request,'donorhomepage.html',context)

def createDonationRequest(request):
    if request.method == 'POST':
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            request = DonationRequest(
                ngo_name=form.cleaned_data.get('ngo_name'),
                project_name=form.cleaned_data.get('project_name'),
                description=form.cleaned_data.get('description'),
                amount=form.cleaned_data.get('amount'),
                )
            request.save()
            return redirect('donation-request')      
    else:
        form = DonationRequestForm()
    return render(request, 'donationrequestform.html', {'form': form})