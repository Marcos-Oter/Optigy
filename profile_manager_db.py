'''import sqlite3

class ProfileManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("data.db", check_same_thread= False)

    def add_Profile(self, id, name, type):
        query = """ INSERT INTO datos (ID, NOMBRE, TIPO)
                    VALUES (?,?,?)
                """
        self.connection()'''
