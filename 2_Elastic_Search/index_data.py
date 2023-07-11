import csv
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
import numpy as np
from faker import Faker
from elasticsearch import Elasticsearch
import joblib
import requests
import random
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

model_path = os.getenv('MODEL_PATH') # ⬅️ .env = chemin complet vers ../1_Analyse/data/bow_model.pkl
csv_path = os.getenv('CSV_PATH') # ⬅️ .env = chemin complet vers ../1_Analyse/data/gold.csv
print(model_path)
###################################### Elactic Search init

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])     # Connexion
index = 'notes'  
# Fonction pour supprimer les documents

def delete_documents(index):
    """
    Definit la requête pour supprimer les documents
    """
    url = f'http://localhost:9200/{index}/_delete_by_query'
    query = {
        "query": {
            "match_all": {}
        }
    }
    response = requests.post(url, json=query)

    if response.status_code == 200:
        print("Suppression des documents terminée.")
    else:
        print("Erreur lors de la suppression des documents.")

delete_documents(index) # Suppression des documents

with open(model_path, 'rb') as f: # Charger le pipeline
    model = joblib.load(f)

fake = Faker() # Instanciation

############################################# Liste des patients

patients = []

for _ in range(200):
    patient_lastname, patient_firstname = fake.last_name(), fake.first_name()
    patients.append((patient_lastname, patient_firstname))

csv_file = csv_path # Chemin vers le fichier CSV

with open(csv_file, 'r') as file:       # Lecture du fichier CSV et indexation des données
    reader = csv.DictReader(file)
    count = 0  # Compteur de documents indexés

    for row in reader:
        patient = random.choice(patients)   # Génération des valeurs Faker pour les champs nom et prenom
        row['patient_firstname'] = patient[1]
        row['patient_lastname'] = patient[0]
        row['emotion'] = model.predict([row['Text']])[0]
        row['confidence'] = model.predict_proba([row['Text']]).max()
        row['date'] =  fake.date_between(start_date='-365d', end_date='today').strftime("%Y-%m-%d")
        row['patient_left'] = fake.boolean()
        es.index(index=index, document=row)        # Indexation des données dans Elasticsearch
        count += 1
        if count % 100 == 0:
            print(f"Nombre total de documents indexés : {count}")        

print(f"Indexation terminée. Nombre total de documents indexés : {count}")