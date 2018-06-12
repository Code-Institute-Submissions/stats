from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
import requests
import json
# Create your views here.
def index(request):
    #return HttpResponse('Posts')
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html',context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)

def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'posts/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I'  # Don't do this! This is just an example. Secure your keys properly.
    })

def league_table(request):
    API_KEY = 'dc67745bd580bab8340e0df81f66f3f4add172b0d7a1c4c329b3783d5f3fb850'
    url = 'https://apifootball.com/api/?action=get_leagues&country_id=169&APIkey='+API_KEY

    jsonList = []
    req = requests.get(url)
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        # userData['country_id'] = data['country_id']
        userData["country_name"] = data["country_name"]
    parsedData.append(userData)
    return HttpResponse(parsedData)