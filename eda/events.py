import datetime

class Event:
    status = "Incomplete"
    def to_txt(self):
        return self.__class__.__name__ + " " + str(vars(self)) + "\n"

class PostEvent(Event):
    str:id
    str:platoform
    datetime.timedelta:delivery_time
    str:text
    datetime.timedelta:frequency
    str:user_id

class NotifyEvent(PostEvent):
    str:email
