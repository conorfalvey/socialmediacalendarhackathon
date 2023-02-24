from app.services.post_service import PostService
from app.services.platform_service import PlatformService
from app.services.user_service import UserService
from app.database.utils.utils import DatabaseContext
from datetime import timedelta

dbc = DatabaseContext()
ps = PostService()
pls = PlatformService()
us = UserService()

delivery_time = timedelta(days=1)
post_text = "Sample post text"
frequency = timedelta(hours=1)

pls.upload_platform("Test Plat", 256)
plat_id = pls.get_all_platform_detail_from_platform_name("Test Plat")[0]

us.create_user(
    name="Test User", email="test@test.com", password="123456789", default_delay="1 day"
)
user_id = us.get_user_by_name(name="Test User")[0].__str__()

ps.upload_post(
    platform=plat_id,
    delivery_time=delivery_time,
    post_text=post_text,
    frequency=frequency,
    user=user_id,
)
post_id = ps.get_all_post_detail_from_platform_and_user(
    platform_id=plat_id, user_id=user_id
)[0].__str__()
print(post_id)

ps.remove_post(post_id=post_id)
