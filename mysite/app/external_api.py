import requests
import base64
from requests.auth import HTTPBasicAuth


# Note, in production this data would be encrypted
COMPANIES_HOUSE_KEY = '1ae6053d-cfe4-49eb-9fae-2d8834c634ac' # not working in live
MY_KEY = '8b5ef71d-4a50-402f-a372-f7a3a4b12d21' # new key generated
TARIFFSCANNER_KEY = 'FtNdbL*B6$9ZNq'

class AddressLookupAPI:
    POSTCODES_BASE_URL = "https://api.ideal-postcodes.co.uk/v1/autocomplete/addresses"
    POSTCODES_KEY = "ak_lt21qifpaE8hyWiA9lsLS9t1vPmr4"

    def lookup(self, postcode):
        # Note, using the key as a querystring parameter is not secure, instead we need to use the 
        # basic Headers authentication but I couldn't get tis working in the postcodes lookup.
        api_url = f"{self.POSTCODES_BASE_URL}?query={postcode}&api_key={self.POSTCODES_KEY}"

        try:
            # Make the API call
            response = requests.get(api_url)
            print(response.status_code)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                return data, postcode
            else:
                # If the request was unsuccessful, return None
                return None
        except Exception as e:
            # Handle exceptions
            print(e)
            return None
        

class CompanyLookupAPI:
    COMPANIES_HOUSE_BASE_URL = "https://api.company-information.service.gov.uk/search/companies"
    COMPANIES_HOUSE_KEY = "a732b3cb-1c69-4f03-8573-a0e55b93f937"  
        
    def lookup_with_query(self, query):
        api_url = f"{self.COMPANIES_HOUSE_BASE_URL}?q={query}"
        print(api_url)

        # Auth variables
        username = self.COMPANIES_HOUSE_KEY
        password = ""  

        try:
            # Make a GET request to the API with basic authentication
            response = requests.get(api_url, auth=(username, password))
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                return data
            else:
                # If the request was unsuccessful, return None
                return None
        except Exception as e:
            # Handle exceptions
            print(e)
            return None

    
