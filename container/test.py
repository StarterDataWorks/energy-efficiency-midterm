import requests

# L'indirizzo del tuo endpoint Flask
url = 'http://localhost:9696/predict'

# Un esempio di dati di un edificio (le 8 feature)
client = {
    "X1": 0.74, 
    "X2": 514.5, 
    "X3": 294.0, 
    "X4": 110.25, 
    "X5": 7.0, 
    "X6": 2, 
    "X7": 0.0, 
    "X8": 0
}

# Inseriamo la richiesta POST inviando il dizionario come JSON
response = requests.post(url, json=client)

# Stampiamo la risposta ricevuta dall'API
print(response.json())