from database.schema import create_tables
from fetcher import fetch_feeds

def main():
    print("Hello from feedix!")
    print("Create tables")
    create_tables()
    print("Fetch Feeds")
    fetch_feeds()



if __name__ == "__main__":
    main()
