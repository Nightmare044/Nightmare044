import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    appid = '29612e15df8d0d08f332cafc69daf449'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    #transfer files to HTML
    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
