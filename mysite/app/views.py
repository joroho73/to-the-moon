from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .external_api import AddressLookupAPI, CompanyLookupAPI  # Import the API Lookup classes


def company(request):
    return render(request=request, template_name="company_signup.html")


class CompanySignupView(View): #Inherit from View
    def get(self, request):
        return render(request, 'company_signup.html')

# Address look up 
class AddressLookupView(View):
    def get(self, request):
        postcode = request.GET.get('postcode')
        
        # Instantiate the AddressLookupAPI class
        address_lookup_api = AddressLookupAPI()
        
        # Call the lookup method of AddressLookupAPI to fetch data from the API
        response_data = address_lookup_api.lookup(postcode)
        print(response_data)
    
        if response_data:
            suggestions = self.process_addresses(response_data)
            print(suggestions)
            return render(request, 'address_lookup.html', {'postcode': postcode, 'suggestions': suggestions})
        else:
            return JsonResponse({'error': 'Failed to fetch data from API'}, status=500)
        

    def process_addresses(self, response_data):
        try:
            hits = response_data[0]['result']['hits']  # Assuming response_data is a tuple containing a dictionary at index 0
            suggestions = [{'address_id': hit['udprn'], 'suggestion': hit['suggestion']} for hit in hits]
            return suggestions
        except (IndexError, KeyError):
            return []  # Return an empty list if there's an error accessing the data


# Company look up
class CompanyLookupView(View):
    def get(self, request):
        address = request.GET.get('address')
        address_id = request.GET.get('address_id')
        return render(request, 'company_lookup.html', {'address': address, 'address_id': address_id})
    
    def post(self, request):
        # Handle POST request to process submitted adress data
        print("CompanyLookupView POST")
        address = request.POST.get('selected_address')
        address_id = request.POST.get('address_id')
        postcode = request.POST.get('postcode')

        # Instantiate the CompanyLookupAPI class
        companies_lookup_api = CompanyLookupAPI()
        
        # Call the lookup method of AddressLookupAPI to fetch data from the API
        # this version uses the postcode specified because it seems to be a little more accurate 
        # than using the address.
        response_json = companies_lookup_api.lookup_with_query(postcode)
        response_json_by_address = companies_lookup_api.lookup_with_query(address)
        #print(response_json_by_address)

        if response_json:
            return render(request, 'company_lookup.html', {'address_id' : address_id, 'address' : address, 'postcode': postcode, 'response_data': response_json, 'response_data_by_address':response_json_by_address })
        else:
            return render(request, 'error_template.html', {'error': 'Failed to fetch data from API'})

        
        return render(request, 'company_lookup.html', {'address': address, 'address_id': address_id, 'postcode' : postcode, 'response_data': response_data })
        
