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

            pre_prompt = ""

            if article_score >= 0.8:
                prompt = f"""Analyse cet article très pertinent et génère un résumé concis mais complet 
                    en 2-3 phrases. Concentre-toi sur les points clés, les informations nouvelles 
                    ou importantes, et les conclusions principales. Format attendu : [Contexte] 
                    [Info clé] [Conclusion]. Titre: {article_title}. Contenu: {article_description}
                """
            elif article_score >= 0.7:
                prompt = f"""Résume cet article en une phrase unique et informative. Extrait uniquement 
                    l'information la plus importante par rapport au titre. Format: [Sujet] + 
                    [Action clé] + [Impact]. Titre: {article_title}. Contenu: {article_description}
                """
            else:
                prompt = f"""Génère une phrase très courte (moins de 15 mots) qui capture l'essence. 
                    Sois extrêmement concis. Titre: {article_title}. Contenu: {article_description}
                """

            summary = generate_summary(prompt)
            query.update_article_summary_by_id(("summarized", summary, article_id))

        print(f"Articles Scored: {len(articles_scored)}")
