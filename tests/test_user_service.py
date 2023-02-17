from app.services.user_service import UserService
from app.database.utils.utils import DatabaseContext
from sqlalchemy import text

dbc = DatabaseContext().engine
us = UserService()
name = "Conor Falvey"
email = "conor.falvey22@gmail.com"
password = "ayylmaoboys"
default_notification_time = "1 hour"

us.create_user(
    name=name, email=email, password=password, default_delay=default_notification_time
)

result1 = us.get_user_id_by_email(email=email)
user_id = result1
print(result1)

result2 = us.get_user_id_by_name(name=name)
print(result2)

result3 = us.get_user_by_email(email=email)
print(result3)

result4 = us.get_user_by_name(name=name)
print(result4)

result5 = us.get_user_default_notification(user_id=user_id)
print(result5)

us.delete_user(user_id=user_id)

with dbc.engine.connect() as connection:
    query = "SELECT COUNT(*) FROM users;"
    result = connection.execute(text(query))
    print(result.first()[0])
