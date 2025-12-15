import database.queries as query
import jinja2
import os
from dotenv import load_dotenv

load_dotenv()

def render_markdown():
    articles_summerized = query.get_articles_by_status(("summarized",))

    if articles_summerized:
        data = []
        for article in articles_summerized:
            article_date = article[4]
            article_link = article[5]
            article_summary = article[8]
        
            article_data = {
                "date": article_date,
                "link": article_link,
                "summary": article_summary[1:-1]
            }
            
            data.append(article_data)

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
