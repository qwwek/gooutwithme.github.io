import pywttr


def getforecast(city):
    try:
        wttr = pywttr.Wttr(city)
        weather = wttr.en()
    except:
        return None

    if len(weather.weather) == 0:
        return None
    
    forecast = {
       "temperature": weather.weather[0].hourly[0].temp_c,
       "pressure": weather.weather[0].hourly[0].pressure,
       "humidity": weather.weather[0].hourly[0].humidity
    }

    return forecast


if __name__ == '__main__':
    location = 'KashaKasha'
    print(getforecast(location))
    