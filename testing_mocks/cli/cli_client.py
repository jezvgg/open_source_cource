import questionary
import httpx
import json

 # Adjust this to your FastAPI server URL



class CLI_Client:
    funtion: dict
    BASE_URL = "http://localhost:8000" 

    def __init__(self):
        self.funtion = {
                "Register a new user": self.register_user,
                "Add an item for a user": self.add_item,
                "Get an item for a user": self.get_item,
                "Get all users": self.get_all_usrs
            }
        

    def start_client(self):
        action = self.ask()
        while action != "Exit":
            ansver = self.funtion[action]()
            print(ansver)
            action = self.ask()   


    
    def ask(self):
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Register a new user",
                "Get all users"
                "Add an item for a user",
                "Get an item for a user",
                "Exit"
            ]
        ).ask()
        return action
    
    def get_all_usrs(self):
        response = httpx.get(f"{self.BASE_URL}/")
        users = response.json()
        if response.status_code == 200:
            if len(users)!=0:
                return f"Users: {users}"
            return "No users"
        return "Failed to get alluser."
    

    
    def register_user(self,username=None):
        if username==None:
            username = questionary.text("Enter username:").ask()
        response = httpx.post(f"{self.BASE_URL}/register/{username}")
        if response.status_code == 200:
            return "User registered successfully!"
        return "Failed to register user."
    
    def add_item(self,username=None,file_path=None):
        if username==None:
            username = questionary.text("Enter username:").ask()
        if file_path==None:
            file_path = questionary.text("Enter the path to the file:").ask()
        with open(file_path, "rb") as file:
            response = httpx.post(f"{self.BASE_URL}/add/{username}", files={"file": file})
            if response.status_code == 200:
                return "Item added successfully!"
            return f"Failed to add item: {response.json().get('detail')}"
    

    def get_item(self,username=None):
        if username==None:
            username = questionary.text("Enter username:").ask()
        response = httpx.get(f"{self.BASE_URL}/get/{username}")
        if response.status_code == 200:
            item_data = response.json()
            return "Item data:", json.dumps(item_data, indent=2)
        return f"Failed to get item: {response.json().get('detail')}"
        


    
