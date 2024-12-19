import unittest
from app import app

class TestMembersAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.headers = {"Authorization": "Bearer library123"}

    def test_add_member(self):
        response = self.app.post("/members", json={"name": "Alice"}, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_get_members(self):
        response = self.app.get("/members", headers=self.headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
