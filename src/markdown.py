import database.queries as query
import jinja2
import os
from dotenv import load_dotenv

load_dotenv()

def render_markdown():
    articles_summerized = query.get_articles_by_status(("summarized",))
    articles_summerized.sort(key=lambda tup: tup[7], reverse=True)

    print(type(articles_summerized[0]))

    if articles_summerized:
        data = []
        for article in articles_summerized:
            article_id = article[0]
            article_date = article[4]
            article_link = article[5]
            article_summary = article[8]
        
            article_data = {
                "date": article_date,
                "link": article_link,
                "summary": article_summary            
            }
            
            data.append(article_data)

            query.update_article_status_by_id(("published", article_id))

        #print(f"Articles summerized: {articles_summerized[0][4]}")
        
        env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/")).get_template("template.md")

        render = env.render(data = data)
        output_dir = os.getenv("OUTPUT_DIRECTORY")
        output_file = output_dir + "/" + articles_summerized[0][4] + ".md"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_file,"wt",encoding="utf-8") as q:
            q.write(render)

        print(f"Today article's render into {output_file}")
