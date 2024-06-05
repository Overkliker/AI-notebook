from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

def create_dbsession(db_path=None, **kwargs):
    db_path = 'postgresql://warehouse:warehouse@localhost:5432/warehouse'
    engine = create_engine(db_path)
    SessionClass = sessionmaker(bind=engine)
    return SessionClass()

print(create_dbsession())