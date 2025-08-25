import datetime

from core.objects import User
from core import constants


def calculate_timespent_for(user: User, cats: list, day: datetime.date =datetime.date.today()):
    available_time = (day.day - user.last_calculation_date.day) * constants.DEFAULT_WORKDAY_HOURS
    if available_time > 0:
        for cat in cats:
            cat.balance -= cat.timespent_ratio * available_time
