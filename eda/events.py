import datetime

class Event:
    status = "Incomplete"
    def to_txt(self):
        return self.__class__.__name__ + " " + str(vars(self)) + "\n"

class PostEvent(Event):
    id:str
    platform:str
    delivery_time:datetime.timedelta
    text:str
    frequency:str
    user_id:str

class NotificationEvent(PostEvent):
    email:str
