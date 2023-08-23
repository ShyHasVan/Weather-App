import datetime
import requests 
from django.shortcuts import render

# Create your views here.
def index(request):
    API_KEY = open("API_KEY", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}"

    if request.method == "POST":
        city1 = request.POST['city1']

        if not city1:
           error_message = "Please enter a city name."
           return render(request, "weather_app/index.html", {"error_message": error_message})
        
        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if weather_data1 is None or daily_forecasts1 is None:
           error_message = "City not found or weather data not available."
           return render(request, "weather_app/index.html", {"error_message": error_message})


        context = {"weather_data1" : weather_data1,
                   "daily_forecasts1" : daily_forecasts1}
        
        return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html")
    

def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    try:
        response = requests.get(current_weather_url.format(city, api_key)).json()
        lat, lon = response['coord']['lat'], response['coord']['lon']
        forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

        weather_data = {"city" : city,
                        "country": response['sys']['country'],
                        "temperature" : str(round(response['main']['temp'] - 273.15, 2)) + "°C",
                        "description" : response['weather'][0]['description'],
                        "icon" : response['weather'][0]['icon'],
                        "sunrise": datetime.datetime.fromtimestamp(response['sys']['sunrise']).strftime("%H:%M:%S"),
                        "sunset": datetime.datetime.fromtimestamp(response['sys']['sunset']).strftime("%H:%M:%S"),
                        "wind_speed": str(response['wind']['speed']) + " m/s",
                        "cloudiness": str(response['clouds']['all']) + "%",
                        "rain_3h": str(response['rain']['3h']) + " mm" if 'rain' in response else "N/A",
                        "pressure": str(response['main']['pressure']) + " hPa",
                        "humidity": str(response['main']['humidity']) + "%"
                        }
        
        daily_forecasts = []
        previous_day = datetime.datetime.now().strftime("%A")
        for daily_data in forecast_response['list']:
            day = datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A")
            if day != previous_day:
                daily_forecasts.append({
                    "day": day,
                    "temperature": str(round(daily_data['main']['temp'] - 273.15, 2)),
                    "description": daily_data['weather'][0]["description"],
                    "icon": daily_data['weather'][0]['icon']
                })
                previous_day = day

        return weather_data, daily_forecasts
    except Exception as e:
        print("Error fetching weather data:", str(e))
        return None, None
