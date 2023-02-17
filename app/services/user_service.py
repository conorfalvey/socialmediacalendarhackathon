from app.database.utils.utils import DatabaseContext
from sqlalchemy import text
from uuid import uuid4
import bcrypt


class UserService(object):
    def __init__(self) -> None:
        self.engine = DatabaseContext().engine
        self.table = "users"

    def create_user(self, name, email, password: str, default_delay):
        pass_hash = bcrypt.hashpw(
            password=password.encode("utf-8"), salt=bcrypt.gensalt()
        ).decode("utf-8")
        query = f"INSERT INTO {self.table} (id, name, email, pass_hash, notification_time) VALUES ('{uuid4()}', '{name}', '{email}', '{pass_hash}', '{default_delay}');"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return

    def get_user_id_by_email(self, email):
        query = f"SELECT id FROM {self.table} WHERE email='{email}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def get_user_id_by_name(self, name):
        query = f"SELECT id FROM {self.table} WHERE name='{name}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def get_user_by_email(self, email):
        query = f"SELECT * FROM {self.table} WHERE email='{email}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()

    def get_user_by_name(self, name):
        query = f"SELECT * FROM {self.table} WHERE name='{name}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()

    def get_user_default_notification(self, user_id):
        query = f"SELECT notification_time FROM {self.table} WHERE id='{user_id}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def delete_user(self, user_id):
        query = f"DELETE FROM {self.table} WHERE id='{user_id}';"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return
