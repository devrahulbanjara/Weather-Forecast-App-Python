import requests

api_key = '145c5f5cc7b6719079c76a215871e298'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_fahrenheit = weather_data.json()['main']['temp']
    temp_celsius = int((temp_fahrenheit - 32) * 5/9)

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp_celsius}ºC")
