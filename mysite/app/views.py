from django.shortcuts import render
from .external_api import AddressLookupAPI  # Import the AddressLookup class


class CompanySignupView:
    def get(self, request):
        return render(request, 'company_signup.html')

class AddressLookupView:
    def get(self, request):
        postcode = request.GET.get('postcode')
        address_lookup_api = AddressLookupAPI()
        addresses = address_lookup_api.lookup(postcode)
        return render(request, 'address_lookup.html', {'addresses': addresses})
