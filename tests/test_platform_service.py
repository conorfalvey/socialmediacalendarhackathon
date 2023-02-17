from app.services.platform_service import PlatformService
from app.database.utils.utils import DatabaseContext
from sqlalchemy import text

dbc = DatabaseContext()
ps = PlatformService()
name = "test_platform"
char_limit = 256

ps.upload_platform(name=name, char_limit=char_limit)

result1 = ps.get_all_platform_detail_from_platform_name(platform_name=name)
row_id = result1[0]
print(result1)

result2 = ps.get_all_platform_detail_from_id(row_id=row_id)
print(result2)

result3 = ps.get_char_limit_by_id(row_id=row_id)
print(result3)

result4 = ps.get_char_limit_by_name(platform_name=name)
print(result4)

result5 = ps.get_platform_name_by_id(row_id=row_id)
print(result5)

result6 = ps.get_platform_name_by_name(platform_name=name)
print(result6)

ps.remove_platform(row_id=row_id)

with dbc.engine.connect() as connection:
    query = "SELECT COUNT(*) FROM platforms;"
    result = connection.execute(text(query))
    print(result.first()[0])
