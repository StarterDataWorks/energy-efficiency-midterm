import pickle
from flask import Flask, request, jsonify

# 1. Carichiamo il modello di regressione lineare salvato con pickle
model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

# 2. Inizializziamo l'applicazione Flask
app = Flask('energy')

# 3. Creiamo l'endpoint per la predizione
@app.route('/predict', methods=['POST'])
def predict():
    # Leggiamo i dati inviati in formato JSON dal client
    data = request.get_json()
    
    # Estraiamo le 8 feature geometriche (da X1 a X8) nell'ordine corretto
    features = [
        data['X1'], data['X2'], data['X3'], data['X4'],
        data['X5'], data['X6'], data['X7'], data['X8']
    ]
    
    # Scikit-learn richiede una lista di campioni (array 2D)
    X = [features]
    
    # Eseguiamo la predizione con il modello caricato
    pred = model.predict(X)[0]
    
    # Prepariamo la risposta in formato JSON
    result = {
        'heating_load_prediction': float(pred)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    # Avviamo il server di sviluppo in ascolto sulla porta standard del corso (9696)
    app.run(debug=True, host='0.0.0.0', port=9696)