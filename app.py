from flask import Flask
from flask_graphql import GraphQLView
from models import Base, engine
from schema import schema

app = Flask(__name__)

# Create database tables using the engine
Base.metadata.create_all(engine)  # Use engine instead of Session.bind

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,  # Enable GraphiQL interface for testing
    ),
)

if __name__ == "__main__":
    app.run()
