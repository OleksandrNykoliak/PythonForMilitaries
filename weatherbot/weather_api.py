import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' 
    }
    response = requests.get(base_url, params=params)
    return response.json()

api_key = 'f28af951e85e978f03fbbb1c69c815c1'
city = 'Lviv'
weather_data = get_weather(api_key, city)

for key, value in weather_data.items():
    print(f'{key}: {value}')


