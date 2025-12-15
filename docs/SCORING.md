# Système de scoring des articles RSS

## Principe

Chaque article est évalué par similarité sémantique (spaCy `fr_core_news_md`) entre ses contenus (titre/description) et les mots-clés utilisateur. Les scores individuels sont agrégés en un score final unique.

## Formule de scoring

```
score_final = α × max(S) + (1-α) × mean(S)
```

Où :
- `S` = liste des scores de similarité pondérés par mot-clé
- `α` = 0.4 (poids du meilleur match vs moyenne)

## Calcul détaillé

### 1. Score par mot-clé

```
score_kw = max(sim_titre × 1.5, sim_description) × poids_utilisateur
```

- **Boost titre** : ×1.5 (le titre est plus représentatif)
- **Poids utilisateur** : échelle 1-5 → multiplicateurs [0.5, 0.75, 1.0, 1.5, 2.0]

### 2. Filtre de pertinence

Article rejeté si `max(S) < 0.5`

### 3. Agrégation hybride

```
score_final = 0.4 × max(S) + 0.6 × mean(S)
```

Équilibre entre :
- Récompenser un excellent match unique (max)
- Valoriser la pertinence globale (mean)

## Paramètres par défaut

| Paramètre | Valeur |
|-----------|--------|
| α (ratio hybride) | 0.4 |
| Seuil minimum | 0.5 |
| Boost titre | 1.5 |

## Interprétation des scores spaCy

| Score | Pertinence |
|-------|------------|
| 0.7+ | Forte |
| 0.5-0.7 | Moyenne |
| < 0.5 | Faible |

## Recommandations

- **Mots-clés** : 5-10, de 1 à 3 mots chacun
- **Pondération** : échelle 1-5 étoiles (défaut: 3)
- **Résultat** : top 10 articles triés par score décroissant
