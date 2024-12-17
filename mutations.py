import graphene
from models import Genre, Movie, Session

class CreateGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field('schema.GenreNode')

    def mutate(self, info, name):
        session = Session()
        new_genre = Genre(name=name)
        session.add(new_genre)
        session.commit()
        return CreateGenre(genre=new_genre)


class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()

    genre = graphene.Field('schema.GenreNode')

    def mutate(self, info, id, name=None):
        session = Session()
        genre = session.query(Genre).get(id)
        if not genre:
            raise Exception("Genre not found")
        if name is not None:
            genre.name = name
        session.commit()
        return UpdateGenre(genre=genre)


class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        session = Session()
        genre = session.query(Genre).get(id)
        if not genre:
            raise Exception("Genre not found")
        session.delete(genre)
        session.commit()
        return DeleteGenre(success=True)


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        release_year = graphene.Int()

    movie = graphene.Field('schema.MovieNode')

    def mutate(self, info, title, description=None, release_year=None):
        session = Session()
        new_movie = Movie(title=title, description=description, release_year=release_year)
        session.add(new_movie)
        session.commit()
        return CreateMovie(movie=new_movie)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        release_year = graphene.Int()

    movie = graphene.Field('schema.MovieNode')

    def mutate(self, info, id, title=None, description=None, release_year=None):
        session = Session()
        movie = session.query(Movie).get(id)
        if not movie:
            raise Exception("Movie not found")
        if title is not None:
            movie.title = title
        if description is not None:
            movie.description = description
        if release_year is not None:
            movie.release_year = release_year
        session.commit()
        return UpdateMovie(movie=movie)


class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        session = Session()
        movie = session.query(Movie).get(id)
        if not movie:
            raise Exception("Movie not found")
        session.delete(movie)
        session.commit()
        return DeleteMovie(success=True)


class Mutation(graphene.ObjectType):
    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()


# Attach Mutations to Schema
# schema.mutation = Mutation  # Uncomment if necessary, depending on how your schema is set up
