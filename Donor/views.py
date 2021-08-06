from django.shortcuts import redirect, render,get_object_or_404
from .forms import *
from .models import *
from NGO.models import NGO



# Create your views here.
def home(request):
    return render(request,'view_requests.html')

def viewDonationRequest(request):
    requests = NGO.objects.all()
    context={'requests':requests}
    return render(request,'donorhomepage.html',context)

def singleDonationRequest(request, pk):
    requests = NGO.objects.get(pk=pk)
    return render(request, 'singleDonation.html',{'requests':requests})

# def createDonationRequest(request):
#     if request.method == 'POST':
#         form = DonationRequestForm(request.POST)
#         if form.is_valid():
#             request = DonationRequest(
#                 ngo_name=form.cleaned_data.get('ngo_name'),
#                 project_name=form.cleaned_data.get('project_name'),
#                 description=form.cleaned_data.get('description'),
#                 amount=form.cleaned_data.get('amount'),
#                 )
#             request.save()
#             return redirect('donation-request')      
#     else:
#         form = DonationRequestForm()
#     return render(request, 'donationrequestform.html', {'form': form})

def makeDonation(request):
    if request.method == 'POST':
        form = MakeDonationForm(request.POST)
        if form.is_valid():
            donation = Donation(
                donor_name=form.cleaned_data.get('donor_name'),
                donation_title=form.cleaned_data.get('donation_title'),
                donation_amount=form.cleaned_data.get('donation_amount'),
                description=form.cleaned_data.get('description'),
            )
            donation.save()
            return redirect('donations')
    else:
        form = MakeDonationForm()

    return render(request,'makedonation.html', {'form':form})

def donations(request):
    donations = Donation.objects.all()
    context = {'donations':donations}
    return render(request,'donations.html',context)



# def search_results(request):
        
#     if 'category' in request.GET and request.GET["category"]:
#         search_term = request.GET.get("category")
#         searched_request = DonationRequest.search_by_category(search_term)
#         message = f"{search_term}"
#         return render(request, 'category.html', {"message": message, "requests": searched_request})
#     else:
#         message = "You haven't searched for any"
#         return render(request, 'category.html', {"message": message})

# def search_results(request):
#     """ search function  """
#     if request.method == "POST":
#         query_name = request.POST.get('name', None)
#         if query_name:
#             results = DonationRequest.objects.filter(category__name__icontains=query_name)
#             print(results)
#             return render(request, 'search.html', {"results":results})
#     return render(request, 'category.html')