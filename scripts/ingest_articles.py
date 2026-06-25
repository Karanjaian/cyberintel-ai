from app.ingestion.rss_service import fetch_articles
from app.database.db import SessionLocal
from app.database.article_repository import save_article


def main():
    db = SessionLocal()

    try:
        articles = fetch_articles()

        saved = 0

        for article in articles:
            result = save_article(db, article)

            if result:
                saved += 1

        print(f"Saved {saved} new articles")

    finally:
        db.close()


if __name__ == "__main__":
    main()
