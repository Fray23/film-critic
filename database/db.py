import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self, db_path):
        engine = create_engine('sqlite:///{}'.format(db_path), echo=True)
        self.connect = engine
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=engine)

    def migrate(self):
        self.Base.metadata.create_all(self.connect)


data_db = DB(db_path='data.db')
data_db.migrate()
