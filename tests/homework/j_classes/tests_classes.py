import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_roll_returns_value_in_range(self):
        die = Die()
        for _ in range(3):
            die.roll()
            value = die.get_rolled_value()
            self.assertIn(value, range(1, 7))
