import unittest
from unittest.mock import patch, MagicMock
import httpx
from cli.cli_client import CLI_Client  
import json


class TestCLIClient(unittest.TestCase):


    @patch('httpx.get')
    def test_get_all_users(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = ["user1","user2"]
        client = CLI_Client()

    
        result = client.get_all_usrs()

        user_test=['user1','user2']
        assert result == f"Users: {json.dumps(user_test).replace("\"", "\'")}"


    @patch('httpx.post')
    def test_register_user(self, mock_post):
        mock_post.return_value.status_code = 200
        client = CLI_Client()

        result = client.register_user(username='testuser')

        assert result=="User registered successfully!"

    @patch('httpx.post')
    def test_add_item(self, mock_post):
        mock_post.return_value.status_code = 200
        client = CLI_Client()

        with patch('builtins.open', new_callable=MagicMock):
            result = client.add_item(username='testuser', file_path='dummy_path')


        assert result == "Item added successfully!"

    @patch('httpx.get')
    def test_get_item(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"item": "test_item"}
        client = CLI_Client()

    
        result = client.get_item(username='testuser')

        
        assert result == ("Item data:", json.dumps({"item": "test_item"}, indent=2))

    




