from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.article import Article
from app.ai.summarizer import summarize


def summarize_articles():
    db: Session = SessionLocal()

    try:
        # Get all articles without a summary
        articles = (
            db.query(Article)
            .filter(Article.summary.is_(None))
            .all()
        )

        if not articles:
            print("No articles require summarization.")
            return

        print(f"Found {len(articles)} articles to summarize.\n")

        for article in articles:
            print(f"Summarizing: {article.title}")

            # For now, summarize the title
            summary = summarize(article.title)

            article.summary = summary

            db.commit()

            print("✓ Saved summary\n")

        print("All articles summarized successfully!")

    finally:
        db.close()


if __name__ == "__main__":
    summarize_articles()
