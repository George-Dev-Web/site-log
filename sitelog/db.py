from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sitelog.models import Base

# Create the SQLite database engine

engine = create_engine('sqlite:///sitelog.db', echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
# Create all tables in the database (if they don't exist yet)
def init_db():
    """
    Creates all defined database tables if they don't already exist.
    This function should be run once to set up the database.
    """
    print("Attempting to create database tables...") 
    Base.metadata.create_all(bind=engine)
    print("Database tables created or already existed.") 

# This block makes the init_db() function run when the script is executed directly
if __name__ == "__main__":
    init_db()

session = SessionLocal()
