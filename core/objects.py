import datetime
import struct
import uuid

from core import config


class Object:

    def __init__(self):
        pass

    def to_dict(self):
        return {}

class Category(Object):
    
    def __init__(self, name: str, timespent_ratio: float):
        super().__init__()
        self.name = name
        self.timespent_ratio = timespent_ratio
        self.balance = config.DEFAULT_BALANCE

    def to_dict(self):
        d = super().to_dict()
        d["name"] = self.name
        d["timespent_ratio"] = self.timespent_ratio
        d["balance"] = self.balance
        return d


class Task(Object):
    
    def __init__(self, desc: str, hours_cost: int, cat: Category):
        self.desc = desc
        self.hours_cost = hours_cost
        self.cat = cat
        self.completed = False


class User(Object):

    def __init__(self, workday_hours: int =config.DEFAULT_WORKDAY_HOURS):
        self.workday_hours = workday_hours
        self.last_calculation_date = datetime.date.today()

    def to_dict(self):
        d = super().to_dict()
        d["workday_hours"] = self.workday_hours
        d["last_calculation_date"] = self.last_calculation_date.strftime(config.S11N_DATE_FORMAT)
        return d
