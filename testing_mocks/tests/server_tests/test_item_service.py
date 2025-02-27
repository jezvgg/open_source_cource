import unittest
import io
import json

from fastapi.testclient import TestClient
from fastapi import HTTPException

from app.routers import users_list
from app.routers.items import items as items_list
from app.routers import items_router



class TestUserService(unittest.TestCase):
    client = TestClient(items_router)


    def test_add_item(self):
        with self.assertRaises(HTTPException):
            response1 = self.client.post('/items/add/jezv', 
                                     files={"file": b'"Header1","Header2"\n"value1",2'})
            assert response1.status_code == 404

        users_list.append('jezv')

        response2 = self.client.post('/items/add/jezv', 
                                   files={"file": b'"Header1","Header2"\n"value1",2'})
        
        users_list.remove('jezv')

        assert response2.status_code == 200


    def test_get_item(self):
        with self.assertRaises(HTTPException):
            response1 = self.client.get('/items/get/jezv')

            assert response1.status_code == 404
            
        users_list.append('jezv')
        items_list[users_list[0]] = {'a':2}

        response2 = self.client.get('/items/get/jezv')
        
        del items_list[users_list[0]]
        users_list.remove('jezv')
        

        assert response2.status_code == 200
        assert response2.json() == {'a':2}