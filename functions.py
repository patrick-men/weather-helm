#thermometer function
def thermometer(temp_kelvin):
    #calc weather from kelvin to celsius
    temp_celsius = round(temp_kelvin - 273.15)
    return temp_celsius



#weather icon assignment function - id source https://openweathermap.org/weather-conditions
def weather_icon(id):

    #weather icons
    weather_icons = ["Clear Sky","Cloudy, Overcast","Rain","- Snow","Few Clouds","Slight Rain, Drizzle","Thunderstorm"]

    #create message with icon based on weather id
    if 200 <= id <= 232:
        return weather_icons[6]
    
    elif 600 <= id <= 622:
        return weather_icons[3]
    
    elif id == 800:
        return weather_icons[0]
    
    elif 801 <= id <= 802:
        return weather_icons[4]
    
    elif 803 <= id <= 804:
        return weather_icons[1]
    
    elif id == 500 or 300 <= id <= 301:
        return weather_icons[5]
    
    elif 302 <= id <= 321 or 501 <= id <= 531:
        return weather_icons[2]

def wind_desc(speed):

    #round to one decimal, easier to compare to wind speed metrics
    speed = round(speed, 1)

    #create message based on wind speeds
    if speed < 0.5:
        return f"Almost no wind - {speed} m/s"
    elif 0.5 <= speed <= 3.3:
        return f"Light breeze - {speed} m/s"
    elif 3.4 <= speed <= 5.4:
        return f"Gentle breeze - {speed} m/s"
    elif 5.5 <= speed <= 7.9:
        return f"Moderate breeze - {speed} m/s"
    elif 8.0 <= speed <= 10.7:
        return f"It's getting windy - {speed} m/s"
    elif 10.8 <= speed <= 13.8:
        return f"IT'S FUCKING WINDYYY - {speed} m/s"
    else:
        return f"JESUS FUCK ITS WINDY - {speed} m/s" 

def time_fix(input):
    
    time = input[-8:-2]
    time = time.replace(":","")
    return time

def wind_fix(input):
    
    string = float(input)
    return string