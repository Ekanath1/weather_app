import requests


# Function to fetch weather data
def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
        print(data)
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        wind_speed = data["wind"]["speed"]

        return {
            "city": city_name,
            "temperature": temp,
            "description": weather_desc,
            "humidity": humidity,
            "wind_speed": wind_speed
        }
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Error: Unable to fetch weather data. Please check the city name."


def clothing_suggestion(temperature):
    if temperature < 10:
        return "It's cold! Wear a jacket or coat."
    elif 10 <= temperature < 20:
        return "It's cool. A sweater or light jacket is recommended."
    elif 20 <= temperature < 30:
        return "It's warm. Comfortable casual clothing should be fine."
    else:
        return "It's hot! Wear light, breathable clothing."


print("Welcome to the Weather App!")
api_key = "2812e6b373cc69a8ed7124f407bb531c"

while True:
    city = input("Enter the city name (or type 'exit' to quit): ").strip().lower()
    if city == 'exit':
        print("Thank you for using the Weather App. Goodbye ")
        break

    weather = get_weather(city, api_key)
    if isinstance(weather, dict):
        print(f"\n Weather in {weather['city']}")
        print(f"Temperature: {weather['temperature']}C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']}m/s")
        print(clothing_suggestion(weather["temperature"]))
    else:
        print(weather)

    print("\n")


