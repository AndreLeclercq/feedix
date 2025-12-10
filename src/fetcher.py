import feedparser

d = feedparser.parse('https://www.actuia.com/feed/')
print(d.entries[0].published)
print(d.entries[0])

# TODO: Ouvrir le fichier config/feeds.json
# TODO: Récupérer les feeds
# TODO: Pour chaque feed récupérer les données de la veille pour les placer dans un dictionnaire.
# TODO: Envoyer les données dans la bdd SQlite.
