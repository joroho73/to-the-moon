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
        response_data = address_lookup_api.lookup(postcode)
    
        if response_data:
            suggestions = self.process_addresses(response_data)
            return render(request, 'address_lookup.html', {'postcode': postcode, 'suggestions': suggestions})
        else:
            return render(request, 'error_template.html', {'error': 'Failed to fetch data from API'})

    def process_addresses(self, response_data):
        try:
            hits = response_data[0]['result']['hits']  # Assuming response_data is a tuple containing a dictionary at index 0
            suggestions = [hit['suggestion'] for hit in hits]
            return suggestions
        except (IndexError, KeyError):
            return []  # Return an empty list if there's an error accessing the data


