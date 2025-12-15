import feedparser
import json
import datetime
import requests
from uuid_extensions import uuid7
import database.queries as query

def fetch_feeds():
    with open('config/feeds.json', 'r') as file:
        data = json.load(file)

    feeds = data['feeds']
    total_articles_fetch = 0
    print(f"Total feeds: {len(feeds)}")

    for feed in feeds:
        #print("Current feed: ", feed)
        try:
            get = requests.get(feed, timeout=5)
        except:
            continue

        if not get.status_code == 200:
            print(f"Feed url error on {feed} | Status: {get.status_code}")
            continue

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

            article_exists = query.get_article_by_title((article.title,))

            if article.date_parsed == yesterday and not article_exists:
                todays_articles.append(article)

        if len(todays_articles) > 0:
            total_articles_fetch += len(todays_articles)
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
                    article.description
                ))
    print(f"Articles fetch: {total_articles_fetch}")
