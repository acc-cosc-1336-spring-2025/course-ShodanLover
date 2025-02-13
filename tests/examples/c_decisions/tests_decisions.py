import unittest

from src.examples.c_decisions.decisions import compare_numbers_equality, is_number_in_range, is_vowel, test_config  # Import the function

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
        self.assertEqual(True or False, True)  # Corrected this line
        self.assertEqual(False or True, True)  # Corrected this line
        self.assertEqual(True or True, True)   # Corrected this line

    def test_not_truth_table(self):
        self.assertEqual(not False, True)
        self.assertEqual(not True, False)

    def test_compare_numbers_equality(self):
        self.assertEqual(compare_numbers_equality(10, 5), False)  # Call the actual function
        self.assertEqual(compare_numbers_equality(10, 10), True)  # Call the actual function

    def test_is_number_in_range(self):
        self.assertEqual(is_number_in_range(1, 10, 11), True)

    def test_is_vowel(self):
        self.assertEqual(is_vowel('a'), True)
        self.assertEqual(is_vowel('e'), True)
        self.assertEqual(is_vowel('i'), True)
        self.assertEqual(is_vowel('o'), True)
        self.assertEqual(is_vowel('u'), True)
        self.assertEqual(is_vowel('m'), False)