from typing import Callable

import questionary
import httpx

from cli.enums.choices import Choice




class CLI_Client:
    '''
    Класс реализующий логику CLI.
    Основан на фреймворке questionary и реализует логику взаимодействия с сервервенрой частью.

    :param BASE_URL: Константное значение адреса по которому обращаемся
    :param funtion: Словарь взаимодействий
    '''
    BASE_URL = "http://localhost:8000" 
    funtion: dict[Choice, Callable]


    def __init__(self):
        self.funtion = {
                Choice.REGISTER: self.register_user,
                Choice.ADD_ITEM: self.add_item,
                Choice.GET_ITEM: self.get_item,
                Choice.GET_USERS: self.get_all_usrs
            }
        

    def start_client(self) -> None:
        '''
        Функция для запуска клиента.
        Не ну тут просто угар, ansver, funtion XD
        '''
        action = self.ask()
        while action != Choice.EXIT:
            ansver = self.funtion[action]()
            print(ansver) # Будем думать, что это логгирование, в малом приложении
            action = self.ask()   


    
    def ask(self) -> Choice:
        '''
        Функция реализующая вопрошание. В зависимости от ответа вызывает другие функции из перечня.
        '''
        action = questionary.select(
            "What would you like to do?",
            choices=[
                Choice.REGISTER,
                Choice.GET_USERS,
                Choice.ADD_ITEM,
                Choice.GET_ITEM,
                Choice.EXIT
            ]
        ).ask()
        return action
    

    def get_all_usrs(self) -> str:
        '''
        Функция, реализующая логику, получения всех пользователей.
        '''
        response = httpx.get(f"{self.BASE_URL}/")
        users = response.json()

        if response.status_code != 200: return "Failed to get alluser."
        if len(users)==0:return "No users"
            
        return f"Users: {users}"

    
    def register_user(self, username: str | None = None) -> str:
        '''
        Функция реализующая регистрацию пользователя.

        :param username: Имя пользователя default to None
        '''
        if not username: username = questionary.text("Enter username:").ask()
        response = httpx.post(f"{self.BASE_URL}/register/{username}")

        if response.status_code != 200: return "Failed to register user."
        return "User registered successfully!"

    
    def add_item(self, username: str | None = None, file_path: str | None = None) -> str:
        '''
        Функция добавления csv файла к пользователю.

        :param username: Имя пользователя default to None
        :param file_path: Путь до файла в виде строки default to None
        '''
        if not username: username = questionary.text("Enter username:").ask()
        if not file_path: file_path = questionary.text("Enter the path to the file:").ask()

        with open(file_path, "rb") as file:
            response = httpx.post(f"{self.BASE_URL}/add/{username}", files={"file": file})
            if response.status_code != 200: 
                return f"Failed to add item: {response.json().get('detail')}"
            
            return "Item added successfully!"
    

    def get_item(self, username: str | None = None) -> tuple[str, str]:
        '''
        Функция получения файла привязанного к пользователю.

        :param username: Имя пользователя default to None
        '''
        if not username: username = questionary.text("Enter username:").ask()

        response = httpx.get(f"{self.BASE_URL}/get/{username}")
        if response.status_code != 200:
            return f"Failed to get item: {response.json().get('detail')}"
        
        return "Item data:", response.text
        


    
