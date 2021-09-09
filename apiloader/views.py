from django.http import HttpResponse
from django.shortcuts import render
import requests


CANVAS_ID = 30940
URL_API = "https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/" + str(CANVAS_ID)


def home(request):
    return render(request, "home.html")


def users_display(request):
    i = 1
    all_users = []
    while i < 99:
        URL_USERS = URL_API + "/users?_page=" + str(i)
        response = requests.get(URL_USERS)
        response = response.json()

        if len(response) == 0:
            break
        all_users += response
        i +=1
    return render(request, 'users.html', {"all_users":all_users})


def user_info(request, user_id):
    URL_USER = URL_API + "/users/" + str(user_id)
    user_info = requests.get(URL_USER).json()
    user_cards = requests.get(URL_USER + "/credit-cards").json()
    user_addresses = requests.get(URL_USER + "/addresses").json()
    return render(request, 'user_info.html', {"info":user_info, "cards":user_cards, "addresses":user_addresses})


def cities_display(request):
    i = 1
    all_cities = []
    while i < 99:
        URL_CITIES = URL_API + "/cities?_page=" + str(i)
        response = requests.get(URL_CITIES)
        response = response.json()

        if len(response) == 0:
            break
        all_cities += response
        i +=1
    return render(request, 'cities.html', {"all_cities":all_cities})


def city_info(request, city_id):
    i = 1
    found_city = False
    while i < 99:
        URL_CITIES = URL_API + "/cities?_page=" + str(i)
        response = requests.get(URL_CITIES)
        response = response.json()

        if len(response) == 0:
            break
        for city in response:
            if city["id"] ==city_id:
                found_city = city
                break
        if found_city != False:
            break
        i += 1
    users = []
    for user in found_city["users"]:
        URL_USER = URL_API + "/users/" + str(user)
        user_info = requests.get(URL_USER).json()
        users.append(user_info)
    return render(request, 'city_info.html', {"info":found_city, "users":users})



def search_res(request):
    #request = request.GET
    if 'searchword' in request.GET:
        #print("AA",request.GET)
        term = request.GET['searchword']

        i = 1
        all_cities = []
        while i < 99:
            URL_CITIES = URL_API + "/cities?q=" + str(term) + "&_page=" + str(i)
            response = requests.get(URL_CITIES)
            response = response.json()

            if len(response) == 0:
                break
            all_cities += response
            i +=1

        i = 1
        all_users = []
        while i < 99:
            URL_USERS = URL_API + "/users?q=" + str(term) + "&_page=" + str(i)
            response = requests.get(URL_USERS)
            response = response.json()

            if len(response) == 0:
                break
            all_users += response
            i +=1
        
        return render(request, 'search_results.html', {"all_cities":all_cities, "all_users":all_users})
