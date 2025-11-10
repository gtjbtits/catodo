from datetime import datetime

from core import config

def date(date_str=None, format=config.S11N_DATE_FORMAT):
    return datetime.strptime(date_str, format).date() if date_str else datetime.today().date()


def date_str(date=datetime.today().date(), format=config.S11N_DATE_FORMAT):
    return date.strftime(format)