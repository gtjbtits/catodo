from datetime import datetime

from core import config

def date(date_str=None):
    return datetime.strptime(date_str, config.S11N_DATE_FORMAT).date() if date_str else datetime.today().date()


def date_str(date):
    return date.strftime(config.S11N_DATE_FORMAT)