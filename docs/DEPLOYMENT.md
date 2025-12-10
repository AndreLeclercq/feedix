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
MAX_ARTICLES=20
LOG_LEVEL=INFO
OUTPUT_DIR=/var/feedix/output
```

### Structure Recommandée

```
/production/feedix/
├── .env.prod          # Configuration production
├── config/
│   ├── feeds.json     # Flux RSS
│   └── keywords.txt   # Mots-clés
├── logs/
│   └── feedix.log     # Logs
└── output/
    └── reports/       # Rapports générés
```

## Monitoring

### Vérification des Logs

```bash
# Voir les derniers logs
tail -f logs/feedix.log

# Filtrer les erreurs
grep ERROR logs/feedix.log
```

### Vérification du Rapport

```bash
# Lister les rapports générés
ls -lh output/

# Voir le dernier rapport
cat output/$(ls -t output/ | head -1)
```

## Mise à Jour

```bash
# Mise à jour du code
git pull origin main

# Mise à jour des dépendances
uv pip install -r requirements.txt

# Redémarrer le service (si applicable)
sudo systemctl restart feedix
```

## Sécurité

### Bonnes Pratiques

1. **Clé API Mistral**:
   - Ne jamais commiter dans git
   - Utiliser `.env` et `.gitignore`

2. **Permissions**:
   ```bash
   chmod 700 .env
   chmod 600 config/*
   ```

3. **Sauvegardes**:
   - Sauvegarder régulièrement `output/` et `logs/`
   - Exemple avec tar:
   ```bash
   tar -czvf feedix_backup_$(date +%Y%m%d).tar.gz output/ logs/
   ```

## Performance

### Optimisations Possibles

1. **Cache des flux RSS**:
   - Stocker les articles déjà traités
   - Éviter les doublons

2. **Exécution parallèle**:
   - Utiliser `concurrent.futures` pour les requêtes API

3. **Limitation des requêtes**:
   - Configurer un délai entre les requêtes
   - Respecter les limites de l'API Mistral

## Rollback

En cas de problème:

```bash
# Revenir à la version précédente
git checkout tags/v1.0

# Restaurer les dépendances
uv pip install -r requirements.txt

# Redémarrer
sudo systemctl restart feedix
```
