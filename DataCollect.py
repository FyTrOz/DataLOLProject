import requests
import json
import pandas as pd
import psycopg
from database import *

# Clé d'API Riot (voir pour la mettre a jour en auto)
api_key = "RGAPI-Sd3d2736-b268-4443-8bfe-a4ee8166f6eO"

headers = {
    'X-Riot-Token': api_key
}


LectureJsonPlayer()






# Info des joueurs
gameName = "CapitaineFyTrOz"
tagLine = "COACH"

# Fonction pour récupérer les informations de compte du joueur
def getAccount(gameName, tagLine):
    url_compte = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    compte = requests.get(url_compte, headers=headers).json()
    print(f"Voici les infos du comptes : {compte}")
    return compte

# Fonction pour obtenir les matchs du joueur
def getMatchs(compte,params=None ):
    url_matchs = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{compte['puuid']}/ids"
    matchs = requests.get(url_matchs, headers=headers, params=params).json()
    print(f"Voici l'historique des matchs : {matchs}")
    return matchs

# Fonction pour obtenir
def getData(match):
        url_donnees = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}"
        data = requests.get(url_donnees, headers=headers).json()
        print(f"Voici les infos du match : {data}")
        return data

# Fonction pour obtenir les timings des games
def getTimeLine(match):
    url_timeline = f" https://europe.api.riotgames.com/101/match/vS/matches/{match}/timeline"
    timeline = requests.get(url_timeline, headers=headers).json()
    print(f"Voici la timeline du match : {timeline}")
    return timeline






joueurs = [
    {
        "pseudo": "Florian",
        "role": ["Jungle", "Mid"],
        "gameName": "CapitaineFyTrOz",
        "tagLine": "COACH"
    },
    {
        "pseudo": "Phyphy",
        "role": ["Mid", "ADC"],
        "gameName": "Phyrma",
        "tagLine": "FRAUD"
    }
]
