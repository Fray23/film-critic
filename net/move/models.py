from net.database.db import data_db as db
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


class Country(db.Base):
    __tablename__ = 'countries'

    pk                       = Column(Integer, primary_key=True)
    name                     = Column(String)
    slug                     = Column(String)
    numerical_representation = Column(Integer)

    def __repr__(self):
        return "<Country(pk='{}'>".format(self.pk)


class Genre(db.Base):
    __tablename__ = 'genres'

    pk                       = Column(Integer, primary_key=True)
    name                     = Column(String)
    slug                     = Column(String)
    numerical_representation = Column(Integer)

    def __repr__(self):
        return "<Country(pk='{}'>".format(self.pk)


class Сompany(db.Base):
    __tablename__ = 'companies'

    pk                       = Column(Integer, primary_key=True)
    name                     = Column(String)
    slug                     = Column(String)
    numerical_representation = Column(Integer)
