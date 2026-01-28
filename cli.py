import shutil

from core.objects import User, Category, Task, serialize, deserialize
from core.tools import date_str
from core.logic import calculate_timespent_for
from neural import print_color_bar

def print_balances(current_state_fname):
    me = deserialize(current_state_fname)[0]
    sorted_cats_by_balance = sorted(me.categories, key=lambda category: category.balance)
    for category in sorted_cats_by_balance:
        print_color_bar(category.balance, category.name)
    print(f"       Последний расчет - {date_str(me.last_calculation_date, format="%d.%m.%Y")}")

print_balances("./experiments/current_state.json")