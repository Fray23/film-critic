from db import data_db as db
from sqlalchemy import Column, Integer, String, Boolean

class Move(db.Base):
    __tablename__ = 'moves'

    pk                      = Column(Integer, primary_key=True)
    adult                   = Column(Boolean)
    belongs_to_collection   = Column(String)
    budget                  = Column(Integer)
    genres                  = Column(String)
    homepage                = Column(String)
    idd                     = Column(String)
    imdb_id                 = Column(String)
    original_language       = Column(String)
    original_title          = Column(String)
    overview                = Column(String)
    popularity              = Column(String)
    poster_path             = Column(String)
    production_companies    = Column(String)
    production_countries    = Column(String)
    release_date            = Column(String)
    revenue                 = Column(String)
    runtime                 = Column(String)
    spoken_languages        = Column(String)
    status                  = Column(String)
    tagline                 = Column(String)
    title                   = Column(String)
    video                   = Column(String)
    vote_average            = Column(String)
    vote_count              = Column(String)

    def __repr__(self):
        return "<Move(pk='{}'>".format(self.pk)

db.migrate()
