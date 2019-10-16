import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self, db_path):
        engine = create_engine('sqlite:///{}'.format(db_path), echo=True)
        self.engine = engine
        self.Base = declarative_base()
        session = sessionmaker(bind=engine)
        self.Session = session()

    def migrate(self):
        self.Base.metadata.create_all(self.engine)


data_db = DB(db_path='data.db')

# for create tables
# data_db.migrate()
