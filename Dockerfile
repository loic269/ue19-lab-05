# Utiliser une image officielle Python 3 comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Spécifier la commande par défaut pour exécuter votre programme
CMD ["python", "app.py"]