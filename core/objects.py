import datetime

from core import constants

class Category:
    
    def __init__(self, name: str, timespent_ratio: float):
        self.name = name
        self.timespent_ratio = timespent_ratio
        self.balance = constants.DEFAULT_BALANCE


class Task:
    
    def __init__(self, desc: str, hours_cost: int, cat: Category):
        self.desc = desc
        self.hours_cost = hours_cost
        self.cat = cat
        self.completed = False


class User:

    def __init__(self, workday_hours: int =constants.DEFAULT_WORKDAY_HOURS):
        self.workday_hours = workday_hours
        self.today_hours_remine = workday_hours
        self.last_calculation_date = datetime.date.today()