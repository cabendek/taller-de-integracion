from django.shortcuts import  render
from django.db import models
from tarea_app.models import Character, Episode, Quote
import requests

def get_season(request):
    all_seasons_bb= {}
    all_seasons_bcs= {}

    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    response = requests.get(url)
    episodes = response.json()

    for i in episodes:
        #episode_data = Episode(
        #    id = i['episode_id'],
        #    title = i['title'],
        #    season = i['season'],
        #    episode = i['episode'],
        #    air_date = i['air_date'],
        #    #characters = i['characters'],
        #    series = i['series']
        #)
        #episode_data.save()

        temporada = i['season']
        serie = i['series']

        if serie == 'Breaking Bad':

            if temporada not in list(all_seasons_bb.keys()): 
                all_seasons_bb[temporada] = list()
                all_seasons_bb[temporada].append(i['episode'])

            else:
                all_seasons_bb[temporada].append(i['episode'])
            
        else:
            
            if temporada not in all_seasons_bcs:
                all_seasons_bcs[temporada] = list()
                all_seasons_bcs[temporada].append(i['episode'])

            else:    
                all_seasons_bcs[temporada].append(i['episode'])
            
    return render (request, 'inicial.html', { "all_seasons_bb": all_seasons_bb, 
    "all_seasons_bcs": all_seasons_bcs} )

def search_characters(request):

    all_characters = {}

    name = request.GET['search']
    iguales=False
    contador = 0
    largo_anterior = 0
    while iguales==False:

        url = f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={name}&limit=10&offset={contador*10}'
        response = requests.get(url)
        characters = response.json()

        for i in characters:

            id = i['char_id']
            nombre = i['name']
            occupation = i['occupation']
            img = i['img']
            status = i['status']
            nickname = i['nickname']
            appearance = i['appearance']
            better_call_saul_appearance = i['better_call_saul_appearance']
            portrayed = i['portrayed']
            category = i['category']

            all_characters[id] = {'nombre':nombre, 'ocupacion': occupation,'img':img, 'estado':status, 'apodo':nickname,
            'apariciones':appearance, 'apariciones_bcs': better_call_saul_appearance, 'actor':portrayed, 'categoria': category }
        
        contador += 1
        if largo_anterior == len(all_characters):
            iguales = True
        else:
            largo_anterior = len(all_characters)
    

    return render(request, 'characters/character.html', {'all_characters': all_characters})

def search_quotes(request, name):

    quotes_of_character={}
    url = f'https://tarea-1-breaking-bad.herokuapp.com//api/quote?author={name}'
    print(url)
    response = requests.get(url)
    quotes = response.json()
    

    for i in quotes:
        id = i["quote_id"]
        if name == i["author"]:
            quotes_of_character[id] = i["quote"]

    return quotes_of_character



def character_detail(request, id):

    all_characters ={}        
    
    url = f'https://tarea-1-breaking-bad.herokuapp.com/api/characters/{id}'
    response = requests.get(url)
    characters = response.json()

    for i in characters:

        id = i['char_id']
        nombre = i['name']
        occupation = i['occupation']
        img = i['img']
        status = i['status']
        nickname = i['nickname']
        appearance = i['appearance']
        better_call_saul_appearance = i['better_call_saul_appearance']
        portrayed = i['portrayed']
        category = i['category']
    
    
        quotes_of_character = {}
        nombre2 = nombre.replace(" ","+")
        url2 = f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={nombre2}'
        response2 = requests.get(url2)
        print(response2)
        quotes = response2.json()
        

        for j in quotes:
            print
            id = j["quote_id"]
            if nombre == j["author"]:
                quotes_of_character[id] = j["quote"]
        
        quotes = quotes_of_character
        
        all_characters = {'id': id, 'nombre':nombre, 'ocupacion': occupation,'img':img, 'estado':status, 'apodo':nickname,
        'apariciones':appearance, 'apariciones_bcs': better_call_saul_appearance, 'actor':portrayed, 'categoria': category,
        'frases': quotes }
    

    return render(request, 'characters/character_detail.html', {'character': all_characters})

def season_detail(request, season):
    episode_list = {}
    
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    response = requests.get(url)
    episodes = response.json()
    
    for i in episodes:
        #episode_data = Episode(
        #    id = i['episode_id'],
        #    title = i['title'],
        #    season = i['season'],
        #    episode = i['episode'],
        #    air_date = i['air_date'],
        #    #characters = i['characters'],
        #    series = i['series']

        episodio = i['episode']
        temporada = i['season']
        titulo = i['title']
        id = i['episode_id']
        serie = i['series']
        
        if int(temporada) == season and serie == "Breaking Bad":
            episode_list[episodio]=[titulo, id]    

    return render (
        request, 'temporadas.html', {'n_season': season ,
        'episode_list': episode_list}
    )

def season_detail2(request, season):
    episode_list = {}
    
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    response = requests.get(url)
    episodes = response.json()
    
    for i in episodes:
        #episode_data = Episode(
        #    id = i['episode_id'],
        #    title = i['title'],
        #    season = i['season'],
        #    episode = i['episode'],
        #    air_date = i['air_date'],
        #    #characters = i['characters'],
        #    series = i['series']

        episodio = i['episode']
        temporada = i['season']
        titulo = i['title']
        id = i['episode_id']
        
        if int(temporada) == season:
            episode_list[episodio]=[titulo, id]    

    return render (
        request, 'temporadas_bcs.html', {'n_season': season ,
        'episode_list': episode_list}
    )

def episode_detail(request, id):
    
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    response = requests.get(url)
    episodes = response.json()
    
    for i in episodes:
        #episode_data = Episode(
        #    id = i['episode_id'],
        #    title = i['title'],
        #    season = i['season'],
        #    episode = i['episode'],
        #    air_date = i['air_date'],
        #    #characters = i['characters'],
        #    series = i['series']

        episode_id = i['episode_id']

        if episode_id == id:
            title = i['title'],
            season = i['season'],
            episode = i['episode'],
            air_date = i['air_date'],
            characters = i['characters'],
            series = i['series']
        

    return render (
        request, 'episode_detail.html', 
        {'titulo': title ,
        'temporada': season,
        'n_episodio': episode,
        'air_date': air_date,
        'personajes': characters,
        'serie': series
        })


def character(request):
    
    if request.method=='GET':
        name = request.GET.get('name')
        if not name:
            return render(request, '')
        else:
            all_characters ={}        
            
            url = f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={name}'
            response = requests.get(url)
            characters = response.json()

            for i in characters:

                id = i['char_id']
                nombre = i['name']
                occupation = i['occupation']
                img = i['img']
                status = i['status']
                nickname = i['nickname']
                appearance = i['appearance']
                better_call_saul_appearance = i['better_call_saul_appearance']
                portrayed = i['portrayed']
                category = i['category']
                
                
                quotes_of_character = {}
                nombre2 = nombre.replace(" ","+")
                url2 = f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={nombre2}'
                response2 = requests.get(url2)
                print(response2)
                quotes = response2.json()
                

                for j in quotes:
                    print
                    id = j["quote_id"]
                    if nombre == j["author"]:
                        quotes_of_character[id] = j["quote"]
                
                quotes = quotes_of_character
                
                all_characters = {'id': id, 'nombre':nombre, 'ocupacion': occupation,'img':img, 'estado':status, 'apodo':nickname,
                'apariciones':appearance, 'apariciones_bcs': better_call_saul_appearance, 'actor':portrayed, 'categoria': category,
                'frases': quotes }
            

            return render(request, 'characters/character_detail.html', {'character': all_characters})