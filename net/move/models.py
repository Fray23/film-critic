from net.database.db import data_db as db
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


move_country_table = Table('move_country', db.Base.metadata,
    Column('move_pk', Integer, ForeignKey('moves.pk')),
    Column('country_pk', Integer, ForeignKey('countries.pk'))
)

move_companies_table = Table('move_companies', db.Base.metadata,
    Column('move_pk', Integer, ForeignKey('moves.pk')),
    Column('companies_pk', Integer, ForeignKey('companies.pk'))
)


move_genres_table = Table('move_genres', db.Base.metadata,
    Column('move_pk', Integer, ForeignKey('moves.pk')),
    Column('genres_pk', Integer, ForeignKey('genres.pk'))
)


class Move(db.Base):
    __tablename__ = 'moves'

    pk                      = Column(Integer, primary_key=True)
    adult                   = Column(Boolean)
    belongs_to_collection   = Column(String)
    budget                  = Column(Integer)
    genres                  = relationship('Genre', secondary=move_genres_table, backref='moves')
    homepage                = Column(String)
    idd                     = Column(String)
    imdb_id                 = Column(String)
    original_language       = Column(String)
    original_title          = Column(String)
    overview                = Column(String)
    popularity              = Column(String)
    poster_path             = Column(String)
    production_companies    = relationship('Company', secondary=move_companies_table, backref='moves')
    production_countries    = relationship('Country', secondary=move_country_table, backref='moves')
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
        return "<Move pk='{}'>".format(self.pk)


class Country(db.Base):
    __tablename__ = 'countries'

    pk                       = Column(Integer, primary_key=True)
    name                     = Column(String)
    slug                     = Column(String)
    numerical_representation = Column(Integer)

    def __repr__(self):
        return "<Country pk='{}', name='{}'>".format(self.pk, self.name)


class Genre(db.Base):
    __tablename__ = 'genres'

    pk                       = Column(Integer, primary_key=True)
    name                     = Column(String)
    slug                     = Column(String)
    numerical_representation = Column(Integer)

    def __repr__(self):
        return "<Genre pk='{}', name='{}'>".format(self.pk, self.name)


class Company(db.Base):
    __tablename__ = 'companies'

    pk                       = Column(Integer, primary_key=True)
    name                     = Column(String)
    slug                     = Column(String)
    numerical_representation = Column(Integer)

    def __repr__(self):
        return "<Company pk='{}', name='{}'>".format(self.pk, self.name)

db.migrate()
