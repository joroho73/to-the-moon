# external_api.py

import requests


COMPANIES_HOUSE_KEY = '1ae6053d-cfe4-49eb-9fae-2d8834c634ac'
TARIFFSCANNER_KEY = 'FtNdbL*B6$9ZNq'

class AddressLookupAPI:
    BASE_URL = "https://api.ideal-postcodes.co.uk/v1/autocomplete/addresses"
    POSTCODES_KEY = "ak_lt21qifpaE8hyWiA9lsLS9t1vPmr4"

    def lookup(self, postcode):
        api_url = f"{self.BASE_URL}?postcode={postcode}&api_key={self.POSTCODES_KEY}"

        try:
            # Make the API call
            response = requests.get(api_url)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                print(data)
                return data
            else:
                # If the request was unsuccessful, return None
                return None
        except Exception as e:
            # Handle exceptions
            print(e)
            return None
