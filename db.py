from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sqlite_database = "sqlite:///items.db"

engine = create_engine(sqlite_database, echo=True)
Session = sessionmaker(autoflush=False, bind=engine)

