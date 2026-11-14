# Partiamo da un'immagine ufficiale di Python slim (leggera)
FROM python:3.13-slim

# Installiamo pipenv all'interno del container
RUN pip install pipenv

# Creiamo e impostiamo la cartella di lavoro dentro il container
WORKDIR /app

# Copiamo i file di configurazione delle dipendenze per primi (per sfruttare la cache di Docker)
COPY ["Pipfile", "Pipfile.lock", "./"]

# Installiamo le dipendenze a livello di sistema dentro il container usando pipenv
RUN pipenv install --system --deploy

# Copiamo lo script Python e il modello binario
COPY ["logistic.py", "model.bin", "./"]

# Esponiamo la porta 9696 per permettere le comunicazioni verso l'esterno
EXPOSE 9696

# Definiamo il comando di avvio usando Gunicorn (il server di produzione consigliato nel corso)
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "logistic:app"]