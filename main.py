from sitelog.cli import cli
from sitelog.db import init_db

if __name__ == "__main__":
    init_db()  # Make sure tables exist before CLI runs
    cli()
