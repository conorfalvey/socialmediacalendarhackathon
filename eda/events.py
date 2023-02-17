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

    def __init__(self, bypass=False, **kwargs):
        args = list(kwargs.values())
        if len(args) > 6:
            IOError("Too many arguments!")
    
        if not bypass:
            self.id = args[0]
            self.platform = args[1]
            self.delivery_time = args[2]
            self.text = args[3]
            self.frequency = args[4]
            self.user_id = args[5]

    def to_repr(self):
        return {
            "Id": self.id, 
            "Platform": self.platform,
            "Delivery_Time": self.delivery_time,
            "Text": self.text,
            "Frequency": self.frequency,
            "User_id": self.user_id,
            "Type": "PostEvent",
        }
    
    def __str__(self):
        return str(self.to_repr())

class NotificationEvent(PostEvent):
    email:str

    def __init__(self, bypass=False, **kwargs):
        args = list(kwargs.values())
        if len(args) > 6:
            IOError("Too many arguments!")
    
        if not bypass:
            self.email = args[0]
    
    def to_repr(self):
        return {
            "Email": self.email,
            "Type": "NotificationEvent",
        }