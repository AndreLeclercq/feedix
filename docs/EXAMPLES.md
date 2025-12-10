# Exemples d'Utilisation - Feedix MVP

## Cas d'Usage Concrets

### 1. Surveillance Technologique

**Configuration:**
```json
// config/feeds.json
{
  "feeds": [
    "https://techcrunch.com/feed/",
    "https://blog.mistral.ai/feed/",
    "https://towardsdatascience.com/feed",
    "https://dev.to/feed"
  ]
}
```

**Mots-clés:**
```
// config/keywords.txt
IA
Data Engineering
Python
Open Source
Machine Learning
LLM
```

**Résultat:**
Un rapport quotidien avec les dernières actualités tech pertinentes.

### 2. Veille Sectorielle (Exemple: Santé)

**Configuration:**
```json
{
  "feeds": [
    "https://www.lemonde.fr/sante/rss_full.xml",
    "https://www.lesechos.fr/sante/rss.xml",
    "https://www.futura-sciences.com/sante/rss/"
  ]
}
```

**Mots-clés:**
```
Santé publique
Vaccin
Recherche médicale
IA santé
Télémédecine
```

### 3. Surveillance de Projets Open Source

**Configuration:**
```json
{
  "feeds": [
    "https://github.com/mistralai/mistral-src/releases.atom",
    "https://github.com/pytorch/pytorch/releases.atom",
    "https://github.com/huggingface/transformers/releases.atom"
  ]
}
```

**Mots-clés:**
```
Release
Version
Update
New feature
Bug fix
```

## Exemple de Rapport Généré

```markdown
# Feedix Report - 2024-01-15

## Summary
- Total articles fetched: 42
- Relevant articles found: 8
- Processing time: 1m 23s

## Relevant Articles

### Mistral AI Blog - "Nouveau modèle LLM open-source"
**URL:** https://blog.mistral.ai/new-model
**Date:** 2024-01-14
**Keywords matched:** ["IA", "Open Source", "LLM"]
**Summary:**
> Mistral AI annonce la sortie de son nouveau modèle... (généré par Mistral API)

### TechCrunch - "Data Engineering Trends 2024"
**URL:** https://techcrunch.com/data-trends-2024
**Date:** 2024-01-13
**Keywords matched:** ["Data Engineering"]
**Summary:**
> Les principales tendances en data engineering pour 2024... (généré par Mistral API)

### Towards Data Science - "Python for Data Engineers"
**URL:** https://towardsdatascience.com/python-data-engineers
**Date:** 2024-01-12
**Keywords matched:** ["Python", "Data Engineering"]
**Summary:**
> Comment Python devient l'outil indispensable des data engineers... (généré par Mistral API)

## Statistics
- Most frequent keyword: "Data Engineering" (4 occurrences)
- Average article length: 842 words
- Processing time per article: 5.2s
```

## Configuration Avancée

### Filtrer par Date

Modifiez le code pour ajouter un filtre de date:

```python
# Dans src/filter.py

def filter_by_date(articles, days=7):
    """Filtre les articles des derniers jours"""
    cutoff = datetime.now() - timedelta(days=days)
    return [a for a in articles if a['date'] >= cutoff]
```

### Personnaliser le Template

Modifiez `src/templates/report.md.j2`:

```jinja2
# Feedix Report - {{ report_date }}

## {{ project_name }}

{% for article in articles %}
### {{ article.title }}

**Source:** {{ article.source }}
**Date:** {{ article.date }}

{{ article.summary }}

---

{% endfor %}

**Total:** {{ articles|length }} articles pertinents
```

## Intégration avec d'autres Outils

### 1. Publication Automatique sur WordPress

Utilisez l'API WordPress pour publier le rapport:

```python
import requests
from wordpress_xmlrpc import Client

wp = Client('https://votresite.com/xmlrpc.php', 'user', 'password')
wp.call(blogger.newPost(0, {
    'title': f'Feedix Report - {date}',
    'description': markdown_content,
    'post_status': 'publish'
}))
```

### 2. Notification par Email

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText(markdown_content)
msg['Subject'] = f'Feedix Report - {date}'
msg['From'] = 'feedix@domaine.com'
msg['To'] = 'vous@domaine.com'

with smtplib.SMTP('smtp.domaine.com') as server:
    server.send_message(msg)
```

### 3. Stockage dans une Base de Données

```python
import sqlite3

conn = sqlite3.connect('feedix.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports
    (id INTEGER PRIMARY KEY, date TEXT, content TEXT)
''')

cursor.execute('INSERT INTO reports VALUES (?, ?, ?)', 
               (None, date, markdown_content))
conn.commit()
```

## Bonnes Pratiques

1. **Commencez petit**: 3-5 flux RSS maximum pour le MVP
2. **Mots-clés spécifiques**: Évitez les termes trop génériques
3. **Testez régulièrement**: Vérifiez la qualité des résumés
4. **Archivez les rapports**: Conservez une histoire des rapports
5. **Surveillez les quotas API**: Mistral a des limites gratuites
