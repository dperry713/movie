from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    movies = relationship(
        "Movie", 
        secondary="movie_genres", 
        back_populates="genres"
    )

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(1024))
    release_year = Column(Integer)
    genres = relationship(
        "Genre", 
        secondary="movie_genres", 
        back_populates="movies",
        overlaps="movies"  # Add this to silence the warning
    )

class MovieGenreAssociation(Base):
    __tablename__ = 'movie_genres'
    
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)

# Create the database engine
engine = create_engine('sqlite:///movie_database.db')
Base.metadata.create_all(engine)

# Initialize a sessionmaker
Session = sessionmaker(bind=engine)