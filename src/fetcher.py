import feedparser
import json
import datetime
from uuid_extensions import uuid7
import database.queries as query

def fetch_feeds():
    with open('config/feeds.json', 'r') as file:
        data = json.load(file)

    feeds = data['feeds']

    for feed in feeds:
        todays_articles = []
        feed_parse = feedparser.parse(feed)
        for article in feed_parse.entries:
            yesterday = datetime.date.today() - datetime.timedelta(days=1) 
            if hasattr(article, 'published_parsed') and article.published_parsed:
                article.date_parsed = datetime.date(*article.published_parsed[:3])
            elif hasattr(article, 'updated_parsed') and article.updated_parsed:
                article.date_parsed = datetime.date(*article.updated_parsed[:3])
            else:
                continue

            if article.date_parsed == yesterday:
                todays_articles.append(article)

        if len(todays_articles) > 0:
            channel = feed_parse.feed
            channel_id = query.get_channel_id_by_link((channel.link,))

            if not channel_id:
                channel_id = str(uuid7())
                query.create_channel((channel_id, channel.title, channel.link))
               
            for article in todays_articles:
                article_id = str(uuid7())
                
                query.create_article((
                    article_id,
                    channel_id,
                    "untreated",
                    article.title,
                    article.date_parsed,
                    article.link,
                    article.description,
                    ""
                ))
