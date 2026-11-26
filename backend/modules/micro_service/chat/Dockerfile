FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le répertoire 'app' dans le conteneur
COPY app /app/app


# Exposer le port sur lequel l'application fonctionne
EXPOSE 8000

# Spécifier la commande pour démarrer l'application avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
