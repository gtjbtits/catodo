import unittest
import json
from datetime import timedelta

from core.objects import Task, Category, User, serialize, deserialize
from core.logic import calculate_timespent_for
from core.tools import date, date_str
from core import config


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
            self.assertEqual(d10d_user["last_calculation_date"], date_str(user.last_calculation_date))

    def test_deserialize_single_user(self):
        users = deserialize("./tests/assets/single_user_example.json")
        user = users[0]
        self.assertEqual(user.workday_hours, 2)
        self.assertEqual(user.last_calculation_date, date("28.08.2025"))
        self.assertEqual(user.categories[0].name, "Спорт")
        self.assertEqual(user.categories[0].timespent_ratio, 0.14)
        self.assertEqual(user.categories[0].balance, 0.0)
        self.assertEqual(user.categories[0].tasks[0].desc, "Поднять гирю")
        self.assertEqual(user.categories[0].tasks[0].hours_cost, 1)
        self.assertEqual(user.categories[0].tasks[0].completed, date("04.11.2025"))

    def test_calculate_timespent_for_same_day_0_for_single_cat(self):
        user = User(workday_hours=2)
        user.categories.append(Category(name="Спорт", timespent_ratio=1/6))
        calculate_timespent_for(user, day=date())
        self.assertEqual(user.categories[0].balance, config.DEFAULT_BALANCE)

    def test_calculate_timespent_for_next_day_for_multiple_cat_without_tasks(self):
        cat1 = Category(name="Спорт", timespent_ratio=1/120)
        cat2 = Category(name="Математика", timespent_ratio=4/28)
        user = User(workday_hours=2)
        user.categories += [cat1, cat2]
        day = date() + timedelta(days=1)
        calculate_timespent_for(user, day=day)
        self.assertEqual(cat1.balance, -1/60)
        self.assertEqual(cat2.balance, -4/14)

    def test_calculate_timespent_for_week_for_single_cat_with_complete_task(self):
        user = User(workday_hours=4)
        user.categories.append(Category(name="Программирование", timespent_ratio=2/(7*4)))
        user.categories[0].tasks.append(Task(desc="Дописать базовый функционал catodo", hours_cost=2))
        user.categories[0].tasks[0].completed = date() + timedelta(days=3)
        day = date() + timedelta(days=7)
        calculate_timespent_for(user, day=day)
        self.assertEqual(user.categories[0].balance, 0)


if __name__ == "__main__":
    unittest.main()
