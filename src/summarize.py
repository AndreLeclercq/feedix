import database.queries as query
from mistral_api import generate_summary
import json

def summarize_articles():
    articles_scored = query.get_articles_by_status(("scored",))

    if articles_scored:
        for article in articles_scored:
            article_id = article[0]
            article_title = article[3]
            article_description = article[6]
            article_score = article[7]

            pre_prompt = f"""
                Tu es un assistant spécialisé dans la génération de résumés pour un blog.
                **Règles strictes à respecter pour TOUS les résumés :**
                    - Ne jamais inclure de balises (comme [Contexte], [Info clé], etc.) dans la réponse finale.
                    - Ne jamais commenter ta réponse (ex: "Voici un résumé en 10 mots").
                    - Ne pas répéter le titre ou le contenu de l'article.
                    - Respecter strictement le format demandé en fonction du score.
                    - Être concis, précis et orienté vers l'information utile pour le lecteur.
                    - Utiliser un ton neutre et professionnel, adapté à un blog d'actualité.

                **Exemples de sorties attendues :**
                    - Score élevé : "Dans un contexte de crise énergétique, le gouvernement a annoncé un plan de sobriété. Ce plan inclut des mesures contraignantes pour les entreprises. Les experts estiment qu'il pourrait réduire la consommation de 20% d'ici 2027."
                    - Score moyen : "La startup GreenTech lève 30 millions d'euros pour accélérer son projet d'énergie renouvelable."
                    - Score faible : "Nouvelle réglementation sur le recyclage des déchets électroniques."
            """

            if article_score >= 0.8:
                prompt = f"""
                    **Instructions pour ce résumé (score élevé) :**
                        Génère un résumé concis mais complet en 2-3 phrases.
                    Structure ta réponse ainsi :
                        - **Contexte** : [contexte en une phrase]
                        - **Info clé** : [information nouvelle ou importante]
                        - **Conclusion** : [conclusion ou impact principal]

                    **Titre :** {article_title}
                    **Contenu :** {article_description}
                    **Résume :**
                """
            elif article_score >= 0.7:
                prompt = f"""
                    **Instructions pour ce résumé (score moyen) :**
                        Résume cet article en une phrase unique et informative.
                        Format strict : "[Sujet] + [Action clé] + [Impact]".

                    **Titre :** {article_title}
                    **Contenu :** {article_description}
                    **Résume :**

                """
            else:
                prompt = f"""
                    **Instructions pour ce résumé (score faible) :**
                        Génère une phrase très courte (moins de 15 mots) qui capture l'essence de l'article.

                    **Titre :** {article_title}
                    **Contenu :** {article_description}
                    **Résume :**
                """

            summary = generate_summary(pre_prompt + prompt)
            query.update_article_summary_by_id(("summarized", summary, article_id))

        print(f"Articles Scored: {len(articles_scored)}")
