from app.ingestion.rss_service import fetch_articles

articles = fetch_articles()

print(f"Fetched {len(articles)} articles\n")

for article in articles[:5]:
    print(article)
