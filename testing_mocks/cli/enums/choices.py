from enum import StrEnum


class Choice(StrEnum):
    REGISTER = "Register a new user"
    GET_USERS = "Get all users"
    ADD_ITEM = "Add an item for a user"
    GET_ITEM = "Get an item for a user"
    EXIT = "Exit"