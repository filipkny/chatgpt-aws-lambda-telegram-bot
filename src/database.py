from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os


url = URL(
    drivername="postgresql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_ENDPOINT"),
    database=os.getenv("PG_NAME"),
    port=os.getenv("PG_PORT"),
    query={"sslmode": "allow"},
)

engine = create_engine(url)
 
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

Base.metadata.create_all(bind=engine)
