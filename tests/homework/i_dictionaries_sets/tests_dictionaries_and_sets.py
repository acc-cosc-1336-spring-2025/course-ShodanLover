import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertTrue("Widget1" in inventory_dictionary)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {"widget1": 5, "widget2": 10}
        result = remove_inventory_widget(inventory_dictionary, "widget1")
        self.assertEqual(result, "Record deleted")
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertTrue("widget2" in inventory_dictionary)

        result = remove_inventory_widget(inventory_dictionary, "nonexistent_widget")
        self.assertEqual(result, "Item not found")
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertTrue("widget2" in inventory_dictionary)

if __name__ == '__main__':
    unittest.main()