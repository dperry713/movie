import unittest
from app import app
from models import Session, Genre, Movie

class TestMovieDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_create_genre(self):
        response = self.app.post('/graphql', json={'query': 'mutation { createGenre(name: "Action") { genre { id name } } }'})
        data = response.get_json()
        self.assertEqual(data['data']['createGenre']['genre']['name'], "Action")

    def test_create_movie(self):
        response = self.app.post('/graphql', json={'query': 'mutation { createMovie(title: "Inception", description: "A mind-bending thriller", releaseYear: 2010) { movie { id title } } }'})
        data = response.get_json()
        self.assertEqual(data['data']['createMovie']['movie']['title'], "Inception")

    def test_get_genres(self):
        response = self.app.post('/graphql', json={'query': '{ genres { edges { node { id name } } } }'})
        data = response.get_json()
        self.assertIsInstance(data['data']['genres']['edges'], list)

    def test_get_movies(self):
        response = self.app.post('/graphql', json={'query': '{ movies { edges { node { id title } } } }'})
        data = response.get_json()
        self.assertIsInstance(data['data']['movies']['edges'], list)

if __name__ == '__main__':
    unittest.main()
