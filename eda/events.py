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

    def to_repr(self):
        return {
            "Id": self.id, 
            "Platform": self.platform,
            "Delivery_Time": self.delivery_time,
            "Text": self.text,
            "Frequency": self.frequency,
            "User_id": self.user_id
        }

class NotificationEvent(PostEvent):
    email:str
