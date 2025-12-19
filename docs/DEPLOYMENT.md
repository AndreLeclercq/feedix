# Déploiement - Feedix MVP

## Options de Déploiement

### Option 1: Exécution Locale (Recommandé pour MVP)

```bash
# Créer un cron job pour exécution quotidienne
crontab -e

# Ajouter cette ligne pour exécution à 8h tous les jours
0 8 * * * /chemin/vers/feedix/.venv/bin/python /chemin/vers/feedix/src/main.py
```

### Option 2: Déploiement sur PythonAnywhere (Gratuit)

1. Créer un compte sur [PythonAnywhere](https://www.pythonanywhere.com/)
2. Uploader le projet via l'interface web
3. Configurer une tâche planifiée:
   - Menu "Tasks"
   - Ajouter une nouvelle tâche quotidienne
   - Commande: `python /home/tonuser/feedix/src/main.py`

### Option 3: Docker (Pour portabilité)

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install uv && \
    uv pip install --system -r requirements.txt

CMD ["python", "-m", "src.main"]
```

Build et exécution:
```bash
docker build -t feedix .
docker run -v $(pwd)/output:/app/output feedix
```

## Configuration de Production

### Variables d'Environnement

```env
# .env.prod
MISTRAL_API_KEY=ta_cle_prod
OUTPUT_DIR=/var/feedix/output
```
