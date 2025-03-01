import unittest
from tests.homework.e_functions import tests_functions

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner().run(suite)
