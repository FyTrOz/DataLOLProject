import psycopg
from anyio.abc import value
from psycopg import sql
from sqlalchemy import except_

import json

# Info pour la BDD
host = "localhost"
dbname = "datalol"
user = "postgres"
password = "@dmin1"

# Fonction pour la création des tables requises
def creatTable():
    try:
        conn = psycopg.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = conn.cursor()

        # Création de la table Players
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Players (
            puuid INT PRIMARY KEY,
            player_name VARCHAR(255),
            gameName VARCHAR(255),
            tagLine VARCHAR(255)
        );
        """)

        # Création de la table Games_info
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Games_info (
            puuid INT PRIMARY KEY,
            new_match_id INT,
            summoner_name VARCHAR(255),
            summoner_id VARCHAR(255),
            summoner_level INT,
            champion_name VARCHAR(255),
            kills INT,
            deaths INT,
            assists INT,
            total_damage_dealt INT,
            total_damage_taken INT,
            total_heal INT,
            gold_earned INT,
            vision_score INT,
            win BOOLEAN,
            end_of_game_result VARCHAR(255),
            game_creation BIGINT,
            game_duration INT,
            game_end_timestamp BIGINT,
            game_mode VARCHAR(255),
            game_name VARCHAR(255),
            game_start_timestamp BIGINT,
            game_type VARCHAR(255),
            game_version VARCHAR(255),
            map_id INT
        );
        """)

        # Création de la table Games
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Games (
            new_match_id INT PRIMARY KEY,
            game_number INT,
            game_date DATE,
            result VARCHAR(255)
        );
        """)

        conn.commit()

        print("Tables créées avec succès!")

    except Exception as e:
        print(f"Erreur lors de la création des tables : {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Lecture du JSON des players
def LectureJsonPlayer():
    try:
        print("Entrée dans la base")
        fileObject = open("player.json", "r")
        jsonContent = fileObject.read().strip()
        aList = json.loads(jsonContent)
        for player in aList:
            print(f"puuid: {player['puuid']} - Player {player['player_name']} - tagLine: {player['tagLine']}")
        fileObject.close()

    except:
        print("Vous ne pouvez pas lire car le fichier et vide ou inexistant")
        pass

#LectureJsonPlayer()


def testPlayer():
    try:
        conn = psycopg.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = conn.cursor()
        print("Entrée dans la base")
        fileObject = open("player.json", "r")
        jsonContent = fileObject.read().strip()
        aList = json.loads(jsonContent)
        for player in aList:
            #print(f"puuid: {player['puuid']} - Player {player['player_name']} - tagLine: {player['tagLine']}")
            sql = "SELECT * FROM Players WHERE puuid = %s"
            puuidObject = player['puuid']
            cursor.execute(sql, (puuidObject,))
            #select = cursor.fetchall()
            #if select:
            #    for value in select:
            #        print(value[0])


            #else:
            #    print("Aucune données dans le select.")

        fileObject.close()

    except:
        print("Vous ne pouvez pas lire car le fichier et vide ou inexistant")
        pass


testPlayer()


    # Charger les données depuis le fichier player.json
def addPlayer():
    with open('player.json', 'r') as file:
        players_json = json.load(file)

    # Connexion à la base de données PostgreSQL
    try:
        conn = psycopg.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = conn.cursor()

        # Parcours des joueurs dans le JSON
        for player in players_json:
            # Vérification si le joueur existe déjà dans la base de données
            cursor.execute("""
            SELECT COUNT(*) FROM Players WHERE puuid = {player['puuid']};
            """,)

            # Si le joueur n'existe pas (count == 0), on l'ajoute
            if cursor.fetchone()[0] == 0:
                cursor.execute("""
                INSERT INTO Players (puuid, player_name, gameName, tagLine) 
                VALUES (%s, %s, %s, %s);
                """, (player['puuid'], player['player_name'], player['gameName'], player['tagLine']))

                print(f"Player {player['player_name']} ajouté à la base de données.")
            else:
                print(f"Player {player['player_name']} déjà présent dans la base de données.")

        # Commit des modifications
        conn.commit()

    except Exception as e:
        print(f"Erreur lors de l'ajout des joueurs : {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()