import unittest

from core.objects import Task, Category


class TestCoreFunctions(unittest.TestCase):
    
    def test_create_category_with_tasks(self):
        cat = Category(name="Спорт", weight=1.0)
        self.assertEqual(cat.name, "Спорт")
        self.assertEqual(cat.weight, 1.0)

        tasks = [
            Task(desc="Поднять гирю", hours_cost=1, cat=cat),
            Task(desc="Опустить гирю", hours_cost=2, cat=cat),
        ]
        self.assertEqual(tasks[0].desc, "Поднять гирю")
        self.assertEqual(tasks[0].hours_cost, 1)
        self.assertEqual(tasks[0].cat, cat)
        self.assertEqual(tasks[1].desc, "Опустить гирю")
        self.assertEqual(tasks[1].hours_cost, 2)
        self.assertEqual(tasks[1].cat, cat)


if __name__ == "__main__":
    unittest.main()
