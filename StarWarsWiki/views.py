import requests
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def fake_request_view(request):
    # Simulation d'une erreur
    error_message = "Une erreur s'est produite lors du traitement de la requête."

    return render(request, 'error.html', {'error_message': error_message})

def characters(request):
    characters = []
    next_url = 'https://swapi.dev/api/people/'

    while next_url:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = response.json()
            characters += data['results']
            next_url = data['next']
        else:
            error_message = 'Une erreur s\'est produite lors de la récupération des personnages de Star Wars.'
            return render(request, 'error.html', {'error_message': error_message})

    # Récupérer le homeworld pour chaque personnage
    for character in characters:
        homeworld_url = character['homeworld']
        homeworld_response = requests.get(homeworld_url)
        
        if homeworld_response.status_code == 200:
            homeworld_data = homeworld_response.json()
            character['homeworld'] = homeworld_data['name']
        else:
            character['homeworld'] = 'Inconnu'

    context = {'characters': characters}
    return render(request, 'characters.html', context)

def films(request):
    url = 'https://swapi.dev/api/films/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        films = data['results']
    else:
        error_message = 'Une erreur s\'est produite lors de la récupération des films de Star Wars.'
        return render(request, 'error.html', {'error_message': error_message})

    context = {'films': films}
    return render(request, 'films.html', context)

def planets(request):
    planets = []
    next_url = 'https://swapi.dev/api/planets/'

    while next_url:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = response.json()
            planets += data['results']
            next_url = data['next']
        else:
            error_message = 'Une erreur s\'est produite lors de la récupération des planets de Star Wars.'
            return render(request, 'error.html', {'error_message': error_message})
        
    context = {'planets': planets}
    return render(request, 'planets.html', context)

def species(request):
    species = []
    next_url = 'https://swapi.dev/api/species/'

    while next_url:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = response.json()
            species += data['results']
            next_url = data['next']
        else:
            error_message = 'Une erreur s\'est produite lors de la récupération des espèces de Star Wars.'
            return render(request, 'error.html', {'error_message': error_message})
    
    for specie in species:
        homeworld_url = specie['homeworld']
        if homeworld_url:
            homeworld_response = requests.get(homeworld_url)
        
            if homeworld_response.status_code == 200:
                homeworld_data = homeworld_response.json()
                specie['homeworld'] = homeworld_data['name']
            else:
                specie['homeworld'] = 'Inconnu'
        else:
            specie['homeworld'] = 'Inconnu'
        
    context = {'species': species}
    return render(request, 'species.html', context)

def starships_vehicles(request):
    starships = []
    next_url_starships = 'https://swapi.dev/api/starships/'
    vehicles = []
    next_url_vehicles = 'https://swapi.dev/api/vehicles/'

    try:
        while next_url_starships:
            response = requests.get(next_url_starships)
            response.raise_for_status()

            data = response.json()
            starships += data['results']
            next_url_starships = data['next']
        
        while next_url_vehicles:
            response = requests.get(next_url_vehicles)
            response.raise_for_status()

            data = response.json()
            vehicles += data['results']
            next_url_vehicles = data['next']
    except requests.exceptions.RequestException as e:
        error_message = 'Une erreur s\'est produite lors de la récupération des données de Star Wars.'
        return render(request, 'error.html', {'error_message': error_message, 'exception_message': str(e)})

    context = {'starships': starships, 'vehicles': vehicles}
    return render(request, 'starships_vehicles.html', context)