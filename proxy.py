import requests

class Proxy:

    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        continente = self.instance.continent
        print("Proxy working ....")
        if continente == "asia":
            response = requests.get("https://restcountries.eu/rest/v2/region/asia")
            print(response.content)
        elif continente == "europe":
            response = requests.get("https://restcountries.eu/rest/v2/region/europe")
            print(response.content)
        else:
            print("Continente no soportado")