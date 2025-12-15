import spacy
import json
import numpy as np
import database.queries as query

def scoring_articles():
    articles_untreated = query.get_articles_by_status(("untreated",))
    articles_scored = 0
    #print("#######################################")
    if articles_untreated:
        nlp = spacy.load("fr_core_news_md")
        with open('config/keywords.json', 'r') as file:
            data = json.load(file)
        keywords = data['keywords']

        for article in articles_untreated:
            article_id = article[0]
            article_title = article[3]
            article_description = article[6]
            keywords_scores_raw = []
            keywords_weight = []

            for keyword, weight in keywords.items():
                keyword_nlp = nlp(keyword)
                article_title_nlp = nlp(article_title)
                article_description_nlp = nlp(article_description)
                nlp_score_title = keyword_nlp.similarity(article_title_nlp)
                nlp_score_description = keyword_nlp.similarity(article_description_nlp)

                #print(f"""----------
                #    Keyword : {keyword} (weight: {weight})
                #    Article Title: {article_title} (spacy score: {nlp_score_title})
                #    Article Description: {article_description} (spacy score: {nlp_score_description})""")

                score_kw_raw = max(nlp_score_title * 1.2, nlp_score_description)
                #print(f"Max score (nlp_title * 1.5, nlp_description): {score_kw_raw}")

                if score_kw_raw >= 0.6:
                    #print("KEYWORD VALID !")
                    keywords_weight.append(weight)
                    keywords_scores_raw.append(score_kw_raw)
                    #print(f"Keyword score raw: {score_kw_raw}")
                    #print(f"Keyword weight: {weight}")
                #print("----------")

        
            if len(keywords_scores_raw):
                kw_max = np.array(keywords_scores_raw).max()
                kw_weigt = np.array(keywords_weight)
                kw_mean = np.average(keywords_scores_raw, weights=kw_weigt)
                #print(f"""Article: {article_title} 
                #    => Keywords max: {kw_max}
                #    => Keywords mean: {kw_mean}
                #""")
                final_score = 0.4 * kw_max + 0.6 * kw_mean
                """
                if final_score < 0.55:
                    print("REJECT !")
                elif final_score >= 0.55 and final_score < 0.7:
                    print("Low Relevance")
                elif final_score >= 0.7 and final_score < 0.8:
                    print("Good Relevance")
                else:
                    print("Higly relevant")
                print(f"FINAL SCORE: {final_score}")
                """

                if final_score >= 0.55:
                    articles_scored += 1
                    status = "scored"
                    query.update_article_score_by_id((status, final_score, article_id))
                else:
                    query.delete_article_by_id((article_id,))
            else:
                #print(f"Article: {article_title} => No valid keyword")
                query.delete_article_by_id((article_id,))
            #print("#######################################")
    print(f"Articles scored: {articles_scored}")
