from django.shortcuts import render
from django.views import View
from .external_api import AddressLookupAPI  # Import the AddressLookup class


def company(request):
    return render(request=request, template_name="company_signup.html")


class CompanySignupView(View): #Inherit from View
    def get(self, request):
        return render(request, 'company_signup.html')

class AddressLookupView(View):
    def get(self, request):
        postcode = request.GET.get('postcode')
        
        # Instantiate the AddressLookupAPI class
        address_lookup_api = AddressLookupAPI()
        
        # Call the lookup method of AddressLookupAPI to fetch data from the API
        addresses = address_lookup_api.lookup(postcode)
    
        print(addresses)
        
        if addresses:
            # If data is fetched successfully, pass it to the template for rendering
            return render(request, 'address_lookup.html', {'addresses': addresses})
        else:
            # If there's an error or no data fetched, return an error message
            return render(request, 'error_template.html', {'error': 'Failed to fetch data from API'})




