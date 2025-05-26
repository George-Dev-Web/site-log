from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sitelog.models import Base

# Create the SQLite database engine
engine = create_engine('sqlite:///sitelog.db', echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Create all tables in the database (if they don't exist yet)
def init_db():
    Base.metadata.create_all(bind=engine)
