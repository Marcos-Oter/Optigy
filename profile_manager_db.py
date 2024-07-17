<<<<<<< HEAD
import sqlite3

class ProfileManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("profiles.db", check_same_thread= False)

#------------------------------------------------------------Perfil
    def add_profile(self, name, type):

        query = """ INSERT INTO perfiles (NOMBRE, TIPO)
                    VALUES (?,?)
                """
        query_2 = """ INSERT INTO datos (CONSUMO_TOTAL, CONSUMO_ESP)
                      VALUES (?,?)
                """
        initial_value = 0.0
        self.connection.execute(query, (name,type,))
        self.connection.execute(query_2, (initial_value, 300,))
        self.connection.commit() 

    def get_profile(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM perfiles"
        cursor.execute(query)
        profiles = cursor.fetchall()
        return profiles    
    
    def delete_profile(self, id):
        query = "DELETE FROM perfiles WHERE ID =?"
        self.connection.execute(query, (id,))
        self.connection.commit()
    
    def update_profile(self, name, type, profile_id,):
        query = '''UPDATE perfiles SET NOMBRE =?, TIPO =? WHERE ID =?'''
        self.connection.execute(query, (name, type, profile_id))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

#------------------------------------------------------------General

    def get_general_consumtion(self, profile_id):
        cursor = self.connection.cursor()
        query = "SELECT CONSUMO_TOTAL FROM datos WHERE DATOS_ID =?"
        p = (profile_id,)
        cursor.execute(query, p)
        general_consumtion = cursor.fetchone()
        return general_consumtion[0]
    
    def get_consumtion_esp(self, profile_id):
        cursor = self.connection.cursor()
        query = "SELECT CONSUMO_ESP FROM datos WHERE DATOS_ID =?"
        p = (profile_id,)
        cursor.execute(query, p)
        general_consumtion = cursor.fetchone()
        return general_consumtion[0]
    
    def update_consumtion_esp(self, new_value, profile_id):
        query = '''UPDATE datos SET CONSUMO_ESP =? WHERE DATOS_ID =?'''
        self.connection.execute(query, (new_value, profile_id,))
        self.connection.commit()

#------------------------------------------------------------Habitacion

    def add_room(self, profile_id, name_h, type_h):

        query = """ INSERT INTO habitacion (PROFILE_ID, NOMBRE_H, TIPO_H, CONSUMO_H)
                    VALUES (?,?,?,?)
                """
        initial_value = (0.0)
        self.connection.execute(query, (profile_id, name_h, type_h, initial_value))
        self.connection.commit()

    def get_rooms(self, profile_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM habitacion WHERE PROFILE_ID =?"
        p = (profile_id,)
        cursor.execute(query, p)
        rooms = cursor.fetchall()
        return rooms  
    
    def get_rooms_consumtion (self, profile_id):
            cursor = self.connection.cursor()
            query = "SELECT CONSUMO_H FROM habitacion WHERE PROFILE_ID =?"
            p = (profile_id,)
            cursor.execute(query, p)
            rooms_consumtion = cursor.fetchall()
            values = [fila[0] for fila in rooms_consumtion]
            return values
    
    def update_room(self, name, type, profile_id,):
        query = '''UPDATE perfiles SET NOMBRE =?, TIPO =? WHERE PROFILE_ID =?'''
        self.connection.execute(query, (name, type, profile_id))
        self.connection.commit()

    def update_general_consumition(self, consumition, data_id):
            query = '''UPDATE datos SET CONSUMO_TOTAL =? WHERE DATOS_ID =?'''
            self.connection.execute(query, (consumition, data_id))
            self.connection.commit()

    def get_particular_room_consumtion (self, profile_id):
            cursor = self.connection.cursor()
            query = "SELECT CONSUMO_H FROM habitacion WHERE H_ID =?"
            p = (profile_id,)
            cursor.execute(query, p)
            room_consumtion = cursor.fetchone()
            return room_consumtion[0]
    
    def delete_room(self, h_id):
        query = "DELETE FROM habitacion WHERE H_ID =?"
        self.connection.execute(query, (h_id,))
        self.connection.commit()
#------------------------------------------------------------Elementos de consumo

    def add_element(self, room_id, name_e, amount_e, kwh_e):

        query = """ INSERT INTO elementos (ID_ROOM, NOMBRE_E, CANTIDAD_E, KWH_E)
                    VALUES (?,?,?,?)
                """
        self.connection.execute(query, (room_id, name_e, amount_e, kwh_e))
        self.connection.commit()

    def get_particular_elements_consumtion (self, room_id):
            cursor = self.connection.cursor()
            query = "SELECT CONSUMO_H FROM habitacion WHERE H_ID =?"
            p = (room_id,)
            cursor.execute(query, p)
            elements_consumtion = cursor.fetchone()
            return elements_consumtion[0]
    
    def get_elements(self, h_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM elementos WHERE ID_ROOM =?"
        p = (h_id,)
        cursor.execute(query, p)
        elements = cursor.fetchall()
        return elements 
    
    def delete_element(self, e_id):
        query = "DELETE FROM elementos WHERE ID_E_CONSUMO =?"
        self.connection.execute(query, (e_id,))
        self.connection.commit()
    
    def update_particular_consumition(self, consumition, h_id):
            query = '''UPDATE habitacion SET CONSUMO_H =? WHERE H_ID =?'''
            self.connection.execute(query, (consumition, h_id))
            self.connection.commit()
=======
'''import sqlite3

class ProfileManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("data.db", check_same_thread= False)

    def add_Profile(self, id, name, type):
        query = """ INSERT INTO datos (ID, NOMBRE, TIPO)
                    VALUES (?,?,?)
                """
        self.connection()'''
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
