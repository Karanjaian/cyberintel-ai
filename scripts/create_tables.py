from app.database.db import engine, Base
from app.models.article import Article

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")

