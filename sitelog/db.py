# sitelog/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sitelog.models import Base # Ensure Base is imported from your models file

# Create the SQLite database engine
# echo=True is good for debugging, it shows SQL queries in the console
engine = create_engine('sqlite:///sitelog.db', echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Added common session options

# Create all tables in the database (if they don't exist yet)
def init_db():
    """
    Creates all defined database tables if they don't already exist.
    This function should be run once to set up the database.
    """
    print("Attempting to create database tables...") # This print should now show
    Base.metadata.create_all(bind=engine)
    print("Database tables created or already existed.") # This print should now show

# This block makes the init_db() function run when the script is executed directly
if __name__ == "__main__":
    init_db()