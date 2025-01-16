import json
import weathercom

def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    #print(weatherDetails)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    return humidity, temp, phrase

#weatherReport('Mumbai')