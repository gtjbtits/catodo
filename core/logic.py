import datetime

from core.objects import User
from core import config


def calculate_timespent_for(*users: User, day: datetime.date =datetime.date.today()):
    for user in users:
        available_time = (day.day - user.last_calculation_date.day) * config.DEFAULT_WORKDAY_HOURS
        if available_time > 0:
            for cat in user.categories:
                cat.balance -= cat.timespent_ratio * available_time
