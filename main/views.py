from django.shortcuts import render
import requests
import json

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Japan"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "93aed1e04dmshedd41d18de3124ep1fd009jsn9771c1b3992b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']

    d = data[0]

    print(d)

    context = {
        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical']
    }
    return render(request, 'main/index.html', context)