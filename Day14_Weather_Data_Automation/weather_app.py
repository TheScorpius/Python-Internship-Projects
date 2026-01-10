import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Delhi"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    return response.json()

def generate_report(data):
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
WEATHER REPORT
-------------------------
City: {CITY}, {country}
Generated On: {time}

Weather: {weather}
Temperature: {temp} °C
Feels Like: {feels_like} °C
Humidity: {humidity} %
Wind Speed: {wind_speed} m/s
"""

    with open("weather_report.txt", "w") as file:
        file.write(report)

    print("Weather report generated successfully.")

def main():
    if not API_KEY:
        print("API key not found. Check .env file.")
        return

    data = fetch_weather()

    if data.get("cod") != 200:
        print("Error fetching weather data")
        print(data.get("message"))
        return

    generate_report(data)

if __name__ == "__main__":
    main()