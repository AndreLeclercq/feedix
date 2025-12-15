from database.schema import create_tables
from fetcher import fetch_feeds
from scoring import scoring_articles

def main():
    print("Hello from feedix!")
    print("Create tables")
    create_tables()
    print("Fetch Feeds")
    fetch_feeds()
    print("Scoring and Filtering Feeds")
    scoring_articles()


if __name__ == "__main__":
    main()
