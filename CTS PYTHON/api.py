class WeatherAPI:
    def fetch_data(self):
        data = {
            "main": {"temp": 28.5},
            "weather": [{"description": "clear sky"}]
        }

        print("Weather Report")
        print("Temperature:", data["main"]["temp"])
        print("Condition:", data["weather"][0]["description"])

api = WeatherAPI()
api.fetch_data()