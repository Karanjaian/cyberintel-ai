import feedparser
from app.config.rss_sources import RSS_FEEDS


def fetch_articles():
    articles = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            articles.append(
                {
                    "title": entry.get("title"),
                    "url": entry.get("link"),
                    "source": feed.feed.get("title"),
                }
            )

    return articles
