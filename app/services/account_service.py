from app.database.utils.utils import DatabaseContext
from app.services.platform_service import PlatformService
from sqlalchemy import text
from uuid import uuid4


class AccountService(object):
    def __init__(self):
        self.engine = DatabaseContext().engine
        self.platform_service = PlatformService()
        self.table = "accounts"

    def upload_account(self, username, password, email, platform):
        # TODO: Account verification based on platform
        dummy = f"password {password} hurr durr"

        platform_id = self.platform_service.get_all_platform_detail_from_platform_name(
            platform_name=platform
        )
        if not platform_id:
            print("Failed platform lookup")
            return
        query = f"INSERT INTO {self.table} (id, username, token, email, platform_id) VALUES ('{uuid4()}', '{username}', '{dummy}', '{email}', '{platform_id[0]}');"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return

    def remove_account(self, account_id):
        query = f"DELETE FROM {self.table} WHERE id='{account_id}';"
        with self.engine.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            return

    def get_all_accounts(self, email):
        query = f"SELECT platform FROM {self.table} WHERE email='{email}';"
        with self.engine.connect() as connection:
            results = connection.execute(text(query)).all()
            return results
