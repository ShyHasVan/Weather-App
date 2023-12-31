# Weather-App

This repository hosts the code for a weather application developed using Django that provides real-time weather information and forecasts for various cities. The app leverages the OpenWeatherMap API to retrieve weather data and display it in a user-friendly manner. Users can input a city's name and receive current weather conditions and a 5-day forecast.

The main features of this weather app include:

Real-Time Weather Data: The app fetches up-to-date weather information from the OpenWeatherMap API, including temperature, description, sunrise and sunset times, wind speed, cloudiness, rain, pressure, and humidity.

Forecast Display: Beyond current conditions, the app also offers a 5-day forecast with temperature and weather descriptions for each day. The daily forecast helps users plan ahead based on anticipated weather changes.

User-Friendly Interface: The app is designed with a user-friendly interface that allows users to input a city name and quickly retrieve weather data. If the provided city is not found or weather data is unavailable, appropriate error messages are displayed.

Icon Representation: To enhance the visual experience, the app employs weather icons corresponding to the current conditions and forecasts. These icons provide users with a quick visual summary of weather conditions.

Modular Design: The code follows a modular design pattern, separating the logic for fetching weather data and forecasts into distinct functions. This approach promotes code readability, maintainability, and future expansion.

## How to use

### Clone the Repository:
git clone https://github.com/your-username/weather-app.git
cd weather-app

### Get API Key:
You'll need an API key from OpenWeatherMap to access weather data. Save this key in a file named API_KEY in the project's root directory.

### Install Dependencies:
pip install -r requirements.txt

### Run the App:
python manage.py runserver
The app will be accessible at http://127.0.0.1:8000/ in your web browser.

### Search for Weather:
Open the app in your browser.
Enter the name of a city in the input field.
Click the "Get Weather" button.

### View Results:
The app will display the current weather conditions for the city you entered.
You can also view a 5-day forecast to plan ahead.

## Preview
![Screenshot 2023-08-23 152445](https://github.com/ShyHasVan/Weather-App/assets/142844565/3c44d098-3798-4082-a822-7d2cc64ba9ac)

### Notes
Make sure to keep your API key secure. You can use environment variables to manage sensitive information.
This app uses the OpenWeatherMap API, so you might encounter rate limits if used extensively.
Feel free to customize the app's appearance, add new features, or adapt it to your needs.
Enjoy using the Weather App! If you have any questions or suggestions, please feel free to create an issue.

Remember to replace your-username with your actual GitHub username. This README provides a basic guide for users to clone, install dependencies, run the app, and interact with it. You can customize it further based on your app's specific features and user needs.





