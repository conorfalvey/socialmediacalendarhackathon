from app.database.utils.utils import DatabaseContext
from sqlalchemy import text
from uuid import uuid4
from hashlib import md5


class PostService(object):
    def __init__(self):
        self.engine = DatabaseContext().engine
        self.table = "posts"

    def upload_post(self, platform, delivery_time, post_text, frequency, user) -> None:
        post_hash = md5(post_text.encode("utf-8"))
        query = f"INSERT INTO {self.table} (id, delivery_time, text, post_hash, frequency, platform_id, user_id) VALUES ('{uuid4()}', '{delivery_time}', '{post_text}', '{post_hash}', '{frequency}', '{platform}', '{user}');"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return

    def remove_post(self, post_id):
        query = f"DELETE FROM {self.table} WHERE id='{post_id}';"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return

    def get_all_post_detail_from_platform_and_user(self, platform_id, user_id):
        query = f"SELECT * FROM {self.table} WHERE platform_id='{platform_id}' AND user_id='{user_id}';"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.first()
