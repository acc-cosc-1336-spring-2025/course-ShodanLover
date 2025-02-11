import unittest

from src.examples.c_decisions.decisions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):

        self.assertEqual(False and False, False)
        self.assertEqual(True and False, False)
        self.assertEqual(False and True, False)
        self.assertEqual(True and True, True)

    def test_truth_table(self):

    self.assertEqual(False or False, False)
    self.assertEqual(True or False, False)
    self.assertEqual(False and True, False)
    self.assertEqual(True and True, True)

    def test_not_truth_table(self):

    self.assertEqual(not False, True)
    self.assertEqual(not True, False)
