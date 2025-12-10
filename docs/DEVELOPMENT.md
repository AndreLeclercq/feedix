# Guide de Développement - Feedix MVP

## Prérequis

- Python 3.10+
- uv (pour la gestion des dépendances)
- Clé API Mistral (gratuit pour le MVP)

## Installation

```bash
# Cloner le projet
git clone https://github.com/tu-utilisateur/feedix.git
cd feedix

# Créer l'environnement virtuel avec uv
uv venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Installer les dépendances
uv pip install -r requirements.txt
```

## Configuration

### 1. Fichier `.env`

```env
MISTRAL_API_KEY=ton_cle_api_ici
MAX_ARTICLES=10
OUTPUT_DIR=output
```

### 2. Fichier `config/feeds.json`

```json
{
  "feeds": [
    "https://techcrunch.com/feed/",
    "https://blog.mistral.ai/feed/",
    "https://towardsdatascience.com/feed"
  ]
}
```

### 3. Fichier `config/keywords.txt`

```
IA
Data Engineering
Python
Open Source
Machine Learning
```

## Exécution

```bash
# Exécution manuelle
python -m src.main

# Exécution avec logging
python -m src.main --verbose

# Pour une exécution quotidienne (cron)
0 8 * * * /chemin/vers/feedix/.venv/bin/python /chemin/vers/feedix/src/main.py
```

## Structure du Code

```
src/
├── main.py              # Point d'entrée
├── fetcher.py           # Récupération des flux
├── filter.py            # Filtrage par mots-clés
├── mistral.py           # Intégration API Mistral
└── generator.py         # Génération Markdown
```

## Développement

### Ajouter un nouveau flux RSS

1. Éditer `config/feeds.json`
2. Ajouter l'URL dans le tableau `feeds`

### Ajouter des mots-clés

1. Éditer `config/keywords.txt`
2. Ajouter un mot-clé par ligne

### Modifier le template de sortie

1. Éditer `src/templates/report.md.j2`
2. Utiliser la syntaxe Jinja2

## Tests

```bash
# Exécuter les tests
python -m pytest tests/

# Exécuter un test spécifique
python -m pytest tests/test_fetcher.py
```

## Bonnes Pratiques

1. **Commit Messages**: Utiliser le format conventionnel
   - `feat: ajouter nouveau flux RSS`
   - `fix: corriger bug filtrage`
   - `docs: mettre à jour README`

2. **Branches**:
   - `main`: version stable
   - `dev`: développement en cours
   - `feature/*`: nouvelles fonctionnalités

3. **Pull Requests**:
   - Toujours créer une PR vers `dev`
   - Ajouter une description claire
   - Lier à un issue si applicable

## Dépannage

### Problèmes courants

1. **Erreur de connexion à l'API Mistral**
   - Vérifier la clé API dans `.env`
   - Vérifier la connexion internet

2. **Flux RSS inaccessible**
   - Vérifier l'URL dans `config/feeds.json`
   - Tester l'URL dans un navigateur

3. **Aucun article trouvé**
   - Vérifier les mots-clés dans `config/keywords.txt`
   - Essayer avec des mots-clés plus larges

### Logging

Les logs sont générés dans `logs/feedix.log` avec le format:
```
[YYYY-MM-DD HH:MM:SS] [LEVEL] message
```

Niveaux de log:
- `INFO`: Exécution normale
- `WARNING`: Problèmes mineurs
- `ERROR`: Erreurs bloquantes
