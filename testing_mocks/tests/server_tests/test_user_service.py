import unittest

from fastapi.testclient import TestClient

from app.routers import users_router, users_list




class TestUserService(unittest.TestCase):
    client = TestClient(users_router)


    def test_get_all_users(self):
        users_list.clear()

        response = self.client.get('/users/')

        assert len(response.json()) == 0
        assert response.json() == []


    def test_register_user(self):
        users_list.clear()

        response = self.client.post('/users/register/jezv')

        assert response.status_code == 200
        assert self.client.get('/users/').json() == ['jezv']