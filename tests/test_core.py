import unittest
from datetime import datetime
import json

from core.objects import Task, Category, User
from core.logic import calculate_timespent_for
from core import config
from core.tools import serialize, deserialize


class TestCoreFunctions(unittest.TestCase):

    def test_create_category_with_tasks(self):
        cat = Category(name="Спорт", timespent_ratio=1.0)
        self.assertEqual(cat.name, "Спорт")
        self.assertEqual(cat.timespent_ratio, 1.0)

        cat.tasks = [
            Task(desc="Поднять гирю", hours_cost=1),
            Task(desc="Опустить гирю", hours_cost=2),
        ]
        self.assertEqual(cat.tasks[0].desc, "Поднять гирю")
        self.assertEqual(cat.tasks[0].hours_cost, 1)
        self.assertEqual(cat.tasks[1].desc, "Опустить гирю")
        self.assertEqual(cat.tasks[1].hours_cost, 2)

    def test_serialize_categories_with_tasks(self):
        user = User(workday_hours=2)
        json_str = serialize(user)
        objects = json.loads(json_str)
        self.assertGreater(len(objects), 0)
        for d10d_user in objects:
            self.assertIn("workday_hours", d10d_user)
            self.assertEqual(d10d_user["workday_hours"], user.workday_hours)
            self.assertIn("last_calculation_date", d10d_user)
            self.assertEqual(d10d_user["last_calculation_date"], user.last_calculation_date.strftime(config.S11N_DATE_FORMAT))

    def test_deserialize_single_user(self):
        users = deserialize("./tests/assets/single_user_example.json")
        user = users[0]
        self.assertEqual(user.workday_hours, 2)
        self.assertEqual(user.last_calculation_date, datetime.strptime("28.08.2025", config.S11N_DATE_FORMAT).date())
        self.assertEqual(user.categories[0].name, "Спорт")
        self.assertEqual(user.categories[0].timespent_ratio, 0.14)
        self.assertEqual(user.categories[0].balance, 0.0)
        self.assertEqual(user.categories[0].tasks[0].desc, "Поднять гирю")
        self.assertEqual(user.categories[0].tasks[0].hours_cost, 1)

    def test_calculate_timespent_for_same_day_0_for_single_cat(self):
        user = User(workday_hours=2)
        user.categories.append(Category(name="Спорт", timespent_ratio=1/6))
        calculate_timespent_for(user, day=datetime.today().date())
        self.assertEqual(user.categories[0].balance, config.DEFAULT_BALANCE)

    def test_calculate_timespent_for_same_day_1_for_multiple_cat(self):
        cat1 = Category(name="Спорт", timespent_ratio=1/120)
        cat2 = Category(name="Математика", timespent_ratio=4/28)
        user = User(workday_hours=2)
        user.categories += [cat1, cat2]
        day = datetime.today().date()
        day = day.replace(day=day.day + 1)
        calculate_timespent_for(user, day=day)
        self.assertEqual(cat1.balance, -1/30)
        self.assertEqual(cat2.balance, -4/7)


if __name__ == "__main__":
    unittest.main()
