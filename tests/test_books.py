import unittest
from app import app

class TestBooksAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.headers = {"Authorization": "Bearer library123"}

    def test_add_book(self):
        response = self.app.post("/books", json={"title": "Book 1", "author": "Author 1"}, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get("/books", headers=self.headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
