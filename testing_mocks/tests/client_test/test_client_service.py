import unittest
from unittest.mock import patch, MagicMock
import json

import httpx

from cli.cli_client import CLI_Client  




class TestCLIClient(unittest.TestCase):


    @patch('httpx.get')
    def test_get_all_users(self, mock_get: MagicMock):
        mock_get.return_value = httpx.Response(200, json=['user1','user2'])
        client = CLI_Client()
    
        result = client.get_all_usrs()

        assert result == f'Users: {["user1","user2"]}'


    @patch('httpx.post')
    def test_register_user(self, mock_post: MagicMock):
        mock_post.return_value = httpx.Response(200)
        client = CLI_Client()

        result = client.register_user(username='testuser')

        assert result=="User registered successfully!"


    @patch('httpx.post')
    def test_add_item(self, mock_post: MagicMock):
        mock_post.return_value = httpx.Response(200)
        client = CLI_Client()

        with patch('builtins.open', new_callable=MagicMock):
            result = client.add_item(username='testuser', file_path='dummy_path')

        assert result == "Item added successfully!"


    @patch('httpx.get')
    def test_get_item(self, mock_get: MagicMock):
        mock_get.return_value = httpx.Response(200, json={"item":"test_item"})
        client = CLI_Client()

        result = client.get_item(username='testuser')

        assert result[0] == "Item data:"
        assert json.loads(result[1]) == {"item": "test_item"}

    




