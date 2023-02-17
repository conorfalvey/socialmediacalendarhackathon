from app.database.utils.utils import DatabaseContext
from sqlalchemy import text
from uuid import uuid4


class PlatformService(object):
    def __init__(self):
        self.engine = DatabaseContext().engine
        self.table = "platforms"

    def upload_platform(self, name: str, char_limit: int) -> None:
        query = f"INSERT INTO {self.table} (id, name, char_limit) VALUES ('{uuid4()}', '{name}', '{char_limit}');"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return

    def get_char_limit_by_name(self, platform_name):
        query = f"SELECT char_limit FROM {self.table} WHERE name='{platform_name}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def get_char_limit_by_id(self, row_id):
        query = f"SELECT char_limit FROM {self.table} WHERE id='{row_id}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def get_platform_name_by_name(self, platform_name):
        query = f"SELECT id FROM {self.table} WHERE name='{platform_name}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def get_platform_name_by_id(self, row_id):
        query = f"SELECT name FROM {self.table} WHERE id='{row_id}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()[0]

    def get_all_platform_detail_from_id(self, row_id):
        query = f"SELECT * FROM {self.table} WHERE id='{row_id}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()

    def get_all_platform_detail_from_platform_name(self, platform_name):
        query = f"SELECT * FROM {self.table} WHERE name='{platform_name}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()

    def remove_platform(self, row_id):
        query = f"DELETE FROM {self.table} WHERE id='{row_id}';"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return
