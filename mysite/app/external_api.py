import requests

class AddressLookupAPI:
    def lookup(self, postcode):
        # Make API call to fetch addresses based on postcode
        api_url = f"https://api.example.com/lookup?postcode={postcode}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Parse the JSON response and extract addresses
            data = response.json()
            addresses = data.get('addresses', [])
            return addresses
        else:
            # Return an empty list if API call fails
            return []