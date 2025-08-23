class Category:
    
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.state = 0


class Task:
    
    def __init__(self, desc: str, hours_cost: int, cat: Category):
        self.desc = desc
        self.hours_cost = hours_cost
        self.cat = cat
        self.completed = False
