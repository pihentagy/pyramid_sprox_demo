from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Table,
    String,
    Text,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    relationship,
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
metadata = Base.metadata

movie_directors_table = Table(
    'movie_director', metadata,
    Column(
        'movie_id',
        Integer,
        ForeignKey('movie.id'),
        primary_key=True,
    ),
    Column(
        'director_id',
        Integer,
        ForeignKey('director.id'),
        primary_key=True,
    ),
)

class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(200))

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship('Genre', backref='movies')
    release_date = Column(Date, nullable=True)

class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    movies = relationship(
        Movie,
        secondary=movie_directors_table,
        backref='directors',
    )

    def __str__(self):
        return self.title
