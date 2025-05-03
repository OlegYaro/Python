import requests
import json

class Parser:
    def __init__(self):
        self.api_key = 'ff4ee7f0-9ba6-4e53-85a1-d89370b0dbc0'
        self.base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    def get_price(self, coin):
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key
        }
        params = {
            'symbol': f'{coin}'
        }
        try:
            response = requests.get(url=self.base_url, headers=headers, params=params)
            return json.loads(response.text)["data"][coin]["quote"]['USD']['price']
        except Exception as e:
            print("Error fetching data:", e)
            return 0