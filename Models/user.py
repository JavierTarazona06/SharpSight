#Data Base
from config.Data_base import data_base
from passlib.hash import bcrypt

class User:

    def __init__(self, email:str, password:str, operation:int, name:str=None, last_name:str=None) -> None:
        self.id = None
        self.name = None
        self.last_name = None
        self.email = str(email)
        self.password = str(password)
        if operation==1:
            self.get_from_DB()
        elif operation==2:
            if (name is None) or (last_name is None):
                raise Exception("No se puede crear usuario ya que el nombre y/o el apellido son nulos")
            else:
                self.post_to_DB(name, last_name)
        else:
            raise Exception(f"No existe operación número {operation}")


    def __str__(self) -> str:
        return f"{self.id}: {self.name} {self.last_name} {self.email}"
    
    def json(self) -> list:
        result = {}
        result["id"] = int(self.id)
        result["nombre"] = str(self.name)
        result["apellido"] = str(self.last_name)
        result["email"] = str(self.email)
        result["password"] = str(self.password)
        return result

    def post_to_DB(self, name, last_name):

        hashed_password = bcrypt.hash(self.password)
        self.password = hashed_password

        db = data_base()
        query = f"insert into users (name_user, last_name_user, email_user, password_user) values ('{name}','{last_name}','{self.email}','{self.password}');"
        db.cursor.execute(query)

        query = f"select id_user from users where email_user='{self.email}';"
        db.cursor.execute(query)
        result_id = db.cursor.fetchone()[0]

        db.connection.commit()

        db.close()
        
        self.id = int(result_id)
        self.name = str(name)
        self.last_name = str(last_name)

        print(f"Usuario {self.email} creado en DB exitosamente")

    def get_from_DB(self):
        
        db = data_base()

        query_hashedPassword = f"select password_user from users where email_user='{self.email}';"
        db.cursor.execute(query_hashedPassword)
        result_hashedPassword = db.cursor.fetchone()

        if result_hashedPassword:
            hashed_password = result_hashedPassword[0]
            is_valid = bcrypt.verify(self.password,hashed_password)
            if is_valid:
                self.password = hashed_password
                print("Clave válida")
            else:
                raise Exception(f"Clave inválida para usuario {self.email}")
        else:
            raise Exception(f"No existe clave para usuario o usuario {self.email}")
        
        query = f"select id_user,name_user,last_name_user from users where email_user='{self.email}';"
        db.cursor.execute(query)
        result = db.cursor.fetchone()

        self.id = int(result[0])
        self.name = str(result[1])
        self.last_name = str(result[2])

        db.connection.commit()

        db.close()

    def update(self, name:str=None, last_name:str=None, email:str=None, password:str=None):

        db = data_base()

        if name is not None:
            query = f"update users set name_user='{name}' where id_user={self.id}"
            db.cursor.execute(query)
            self.name = name
        if last_name is not None:
            query = f"update users set last_name_user='{last_name}' where id_user={self.id}"
            db.cursor.execute(query)
            self.last_name = last_name
        if email is not None:
            query = f"update users set email_user='{email}' where id_user={self.id}"
            db.cursor.execute(query)
            self.email = email
        if password is not None:
            hashed_password = bcrypt.hash(password)
            query = f"update users set password_user='{hashed_password}' where id_user={self.id}"
            db.cursor.execute(query)
            self.password = hashed_password

        db.connection.commit()

        db.close()

    def delete(self):
        
        db = data_base()
        query = f"delete from users where id_user={self.id};"
        db.cursor.execute(query)
        db.connection.commit()
        print(f"Se eliminó el usuario {self.name} exitosamente")
        db.close()