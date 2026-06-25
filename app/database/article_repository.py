from sqlalchemy.orm import Session
from app.models.article import Article


def article_exists(db: Session, url: str):
    return db.query(Article).filter(Article.url == url).first()


def save_article(db: Session, article_data: dict):
    if article_exists(db, article_data["url"]):
        return None

    article = Article(
        title=article_data["title"],
        url=article_data["url"],
        source=article_data["source"]
    )

    db.add(article)
    db.commit()
    db.refresh(article)

    return article
