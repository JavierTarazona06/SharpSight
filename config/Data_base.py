import mysql.connector

class data_base():

    def __init__(self):
        # Parámetros de conexión
        host = 'localhost'  # Dirección del servidor de MySQL
        database = 'sharp_sight'
        user = 'root'
        password = 'root'

        # Establecer la conexión
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)

        self.cursor = self.connection.cursor()

        print(f"Base de datos {database} conectada exitosamente")
    
    def close(self):
        self.cursor.close()
        self.connection.close()
        print(f"Base de datos cerrada exitosamente")
    
    #Create data base and tables from scracth
    def create_data_base(self):
        # Leer el contenido del archivo con el script SQL
        with open('./config/DataBase/Creation_Script_SharpSight.sql', 'r') as file:
            script_creation = file.read()
            self.cursor.execute(script_creation)
        print(f"Script de creación ejecutado exitosamente")

