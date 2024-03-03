import pywttr


def getforecast(city):
    wttr = pywttr.Wttr(city)
    weather = wttr.en()

    print("get forecast")
    
    forecast = {
       "temperature": weather.weather[0].hourly[0].temp_c,
       "pressure": weather.weather[0].hourly[0].pressure,
       "humidity": weather.weather[0].hourly[0].humidity
    }

    return forecast


if __name__ == '__main__':
    location = 'Oslo'
    print(getforecast(location))
