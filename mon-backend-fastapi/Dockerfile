# Utilise l'image Python officielle
FROM python:3.10

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers dans le conteneur
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port utilisé par FastAPI
EXPOSE 8000

# Commande pour démarrer FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
