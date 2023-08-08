from datetime import date
import requests, json
import time
import matplotlib.pyplot as plt
from functions import thermometer, weather_icon, wind_desc, time_fix, wind_fix
from PIL import Image, ImageDraw, ImageFont
import os

#get the valies.yaml values

values-api = os.environ.get("WEATHER_API_KEY")
values-city = os.environ.get("WEATHER_CITY")



#get weather from openweather
base_url = "https://api.openweathermap.org/data/2.5/forecast?"
city = f"{values-city}"
api_key = f"{values-api}"

#set proper url
url = base_url + "q=" + city + "&appid=" + api_key
#http request
response = requests.get(url)




# Program start


#if response is there, get the data
if response.status_code == 200:

    #get data in json
    data = response.json()

    #date
    today = date.today()


    #data collection


    #temp
    first = data['list'][0]['main']['temp']
    second = data['list'][1]['main']['temp']
    third = data['list'][2]['main']['temp']
    fourth = data['list'][3]['main']['temp']
    fifth = data['list'][4]['main']['temp']
    sixth = data['list'][5]['main']['temp']
    seventh = data['list'][6]['main']['temp']
    eighth = data['list'][7]['main']['temp']
    

    #weather state
    first_weather = data['list'][0]['weather'][0]['id']
    second_weather = data['list'][1]['weather'][0]['id']
    third_weather = data['list'][2]['weather'][0]['id']
    fourth_weather = data['list'][3]['weather'][0]['id']
    fifth_weather = data['list'][4]['weather'][0]['id']
    sixth_weather = data['list'][5]['weather'][0]['id']
    seventh_weather = data['list'][6]['weather'][0]['id']
    eighth_weather = data['list'][6]['weather'][0]['id']

    #wind speeds
    first_wind = data['list'][0]['wind']['speed']
    second_wind = data['list'][1]['wind']['speed']
    third_wind = data['list'][2]['wind']['speed']
    fourth_wind = data['list'][3]['wind']['speed']
    fifth_wind = data['list'][4]['wind']['speed']
    sixth_wind = data['list'][5]['wind']['speed']
    seventh_wind = data['list'][6]['wind']['speed']
    eighth_wind = data['list'][6]['wind']['speed']

    first_time = data['list'][0]['dt_txt']
    second_time = data['list'][1]['dt_txt']
    third_time = data['list'][2]['dt_txt']
    fourth_time = data['list'][3]['dt_txt']
    fifth_time = data['list'][4]['dt_txt']
    sixth_time = data['list'][5]['dt_txt']
    seventh_time = data['list'][6]['dt_txt']
    eighth_time = data['list'][7]['dt_txt']
    

    #data preparation


    #thermometer values temp
    first_T = thermometer(first)
    second_T = thermometer(second)
    third_T = thermometer(third)
    fourth_T = thermometer(fourth)
    fifth_T = thermometer(fifth)
    sixth_T = thermometer(sixth)
    seventh_T = thermometer(seventh)
    eighth_T = thermometer(eighth)
    

    #weather icons
    first_ic = weather_icon(first_weather)
    second_ic = weather_icon(second_weather)
    third_ic = weather_icon(third_weather)
    fourth_ic = weather_icon(fourth_weather)
    fifth_ic = weather_icon(fifth_weather)
    sixth_ic = weather_icon(sixth_weather)
    seventh_ic = weather_icon(seventh_weather)
    eighth_ic = weather_icon(eighth_weather)
    

    #wind
    first_w = wind_fix(first_wind)
    second_w = wind_fix(second_wind)
    third_w = wind_fix(third_wind)
    fourth_w = wind_fix(fourth_wind)
    fifth_w = wind_fix(fifth_wind)
    sixth_w = wind_fix(sixth_wind)
    seventh_w = wind_fix(seventh_wind)
    eighth_w = wind_fix(eighth_wind)
    
    #time
    first_time = time_fix(first_time)
    second_time = time_fix(second_time)
    third_time = time_fix(third_time)
    fourth_time = time_fix(fourth_time)
    fifth_time = time_fix(fifth_time)
    sixth_time = time_fix(sixth_time)
    seventh_time = time_fix(seventh_time)
    eighth_time = time_fix(eighth_time)
    
    #individual data listed
    temp = [first_T, second_T, third_T, fourth_T, fifth_T, sixth_T, seventh_T, eighth_T]
    icon = [first_ic, second_ic, third_ic, fourth_ic, fifth_ic, sixth_ic, seventh_ic, eighth_ic]
    wind = [first_w, second_w, third_w, fourth_w, fifth_w, sixth_w, seventh_w, eighth_w]
    timestamps = [first_time, second_time, third_time, fourth_time, fifth_time, sixth_time, seventh_time, eighth_time]


# temperature visualization

plt.plot(timestamps, temp)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature in Bern")
plt.savefig("/shared-data/temperature.png")

plt.clf()

# temp description

width = 85
height = 140
img = Image.new('RGB', (width, height), color='white')

message = f"""{first_time}: {first_T}°C
{second_time}: {second_T}°C
{third_time}: {third_T}°C
{fourth_time}: {fourth_T}°C
{fifth_time}: {fifth_T}°C
{sixth_time}: {sixth_T}°C
{seventh_time}: {seventh_T}°C
{eighth_time}: {eighth_T}°C
"""
imgDraw = ImageDraw.Draw(img)

imgDraw.text((10, 10), message, fill=(0,0,0))

img.save('/shared-data/temperature_description.png')


# wind visualization

plt.plot(timestamps, wind)
plt.xlabel("Time")
plt.ylabel("Wind Speeds")
plt.title("Wind in Bern")
plt.savefig("/shared-data/wind.png")

# wind description

width = 140
height = 140
img = Image.new('RGB', (width, height), color='white')

message = f"""{first_time}: {first_w} m/s
{second_time}: {second_w} m/s
{third_time}: {third_w} m/s
{fourth_time}: {fourth_w} m/s
{fifth_time}: {fifth_w} m/s
{sixth_time}: {sixth_w} m/s
{seventh_time}: {seventh_w} m/s
{eighth_time}: {eighth_w} m/s
"""
imgDraw = ImageDraw.Draw(img)

imgDraw.text((10, 10), message, fill=(0,0,0))

img.save('/shared-data/wind_description.png')

# icon

width = 200
height = 140
img = Image.new('RGB', (width, height), color='white')

message = f"""{first_time}: {first_ic}
{second_time}: {second_ic}
{third_time}: {third_ic}
{fourth_time}: {fourth_ic}
{fifth_time}: {fifth_ic}
{sixth_time}: {sixth_ic}
{seventh_time}: {seventh_ic}
{eighth_time}: {eighth_ic}
"""
imgDraw = ImageDraw.Draw(img)

imgDraw.text((10, 10), message, fill=(0,0,0))

img.save('/shared-data/weather_description.png')
