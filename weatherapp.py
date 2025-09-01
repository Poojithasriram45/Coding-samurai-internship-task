import requests

API_KEY = 'b1c45f5ffd8238e1623bc2c3e4282719'  # Replace with your actual OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius. Use 'imperial' for Fahrenheit.
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()

        name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']

        print(f"\nWeather in {name}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc.capitalize()}")

    except requests.exceptions.HTTPError:
        print("City not found. Please check the city name.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
