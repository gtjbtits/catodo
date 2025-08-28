from datetime import datetime

from core import config


class Object:

    def __init__(self):
        pass

    def to_dict(self):
        return {}
    
    def from_dict(data):
        pass

class Category(Object):
    
    def __init__(self, name: str, timespent_ratio: float):
        super().__init__()
        self.name = name
        self.timespent_ratio = timespent_ratio
        self.balance = config.DEFAULT_BALANCE
        self.tasks = []

    def to_dict(self):
        d = super().to_dict()
        d["name"] = self.name
        d["timespent_ratio"] = self.timespent_ratio
        d["balance"] = self.balance
        d["tasts"] = []
        for task in self.tasks:
            d["tasts"].append(task.to_dict())
        return d
    
    def from_dict(data):
        c = Category(name=data["name"], timespent_ratio=data["timespent_ratio"])
        c.balance = data["balance"]
        c.tasks = []
        for task_data in data["tasks"]:
            c.tasks.append(Task.from_dict(task_data))
        return c


class Task(Object):
    
    def __init__(self, desc: str, hours_cost: int):
        self.desc = desc
        self.hours_cost = hours_cost
        self.completed = False

    def to_dict(self):
        d = super().to_dict()
        d["desc"] = self.desc
        d["hours_cost"] = self.hours_cost
        d["completed"] = self.completed
        return d
    
    def from_dict(data):
        t = Task(desc=data["desc"], hours_cost=data["hours_cost"])
        if "completed" in data:
            t.completed = data["completed"]
        return t


class User(Object):

    def __init__(self, workday_hours: int =config.DEFAULT_WORKDAY_HOURS):
        self.workday_hours = workday_hours
        self.last_calculation_date = datetime.today().date()
        self.categories = []

    def to_dict(self):
        d = super().to_dict()
        d["workday_hours"] = self.workday_hours
        d["last_calculation_date"] = self.last_calculation_date.strftime(config.S11N_DATE_FORMAT)
        d["categories"] = []
        for category in self.categories:
            d["categories"].append(category.to_dict())
        return d
    
    def from_dict(data):
        u = User()
        u.workday_hours = data["workday_hours"]
        u.last_calculation_date = datetime.strptime(data["last_calculation_date"], config.S11N_DATE_FORMAT).date()
        for category_data in data["categories"]:
            u.categories.append(Category.from_dict(category_data))
        return u
