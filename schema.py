import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Genre, Movie

class GenreNode(SQLAlchemyObjectType):
    class Meta:
        model = Genre
        interfaces = (graphene.relay.Node,)

class MovieNode(SQLAlchemyObjectType):
    class Meta:
        model = Movie
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_genres = SQLAlchemyConnectionField(GenreNode.connection)
    all_movies = SQLAlchemyConnectionField(MovieNode.connection)

schema = graphene.Schema(query=Query)