import datetime

from core.objects import User


def calculate_timespent_for(*users: User, day: datetime.date =datetime.date.today()):
    for user in users:
        days_delta = (day.day - user.last_calculation_date.day)
        if days_delta > 0:
            for cat in user.categories:
                cat.balance -= cat.timespent_ratio * days_delta 
                for task in cat.tasks:
                    if task.completed and user.last_calculation_date <= task.completed <= day:
                        cat.balance += task.hours_cost
