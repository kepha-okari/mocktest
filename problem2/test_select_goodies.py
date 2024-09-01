import unittest
from select_goodies import sort_goodies_by_price, find_minimum_difference_goodies

class TestGoodieDistribution(unittest.TestCase):
    
    def test_find_minimum_difference_goodies_case1(self):
        # Test Case 1: Given example with 4 employees
        goodies = {
            "Fitbit Plus": 7980,
            "IPods": 22349,
            "MI Band": 999,
            "Cult Pass": 2799,
            "Macbook Pro": 229900,
            "Digital Camera": 11101,
            "Alexa": 9999,
            "Sandwich Toaster": 2195,
            "Microwave Oven": 9800,
            "Scale": 4999
        }
        num_employees = 4
        
        expected_goodies = [
            ("Fitbit Plus", 7980),
            ("Microwave Oven", 9800),
            ("Alexa", 9999),
            ("Digital Camera", 11101)
        ]
        expected_diff = 3121
        
        sorted_goodies = sort_goodies_by_price(goodies)
        selected_goodies, min_diff = find_minimum_difference_goodies(sorted_goodies, num_employees)
        
        self.assertEqual(selected_goodies, expected_goodies)
        self.assertEqual(min_diff, expected_diff)
    
    def test_find_minimum_difference_goodies_case2(self):
        # Test Case 2: Smaller number of employees (2)
        goodies = {
            "Fitbit Plus": 7980,
            "Microwave Oven": 9800,
            "Alexa": 9999
        }
        num_employees = 2
        
        expected_goodies = [
            ("Microwave Oven", 9800),
            ("Alexa", 9999)
        ]
        expected_diff = 199
        
        sorted_goodies = sort_goodies_by_price(goodies)
        selected_goodies, min_diff = find_minimum_difference_goodies(sorted_goodies, num_employees)
        
        self.assertEqual(selected_goodies, expected_goodies)
        self.assertEqual(min_diff, expected_diff)
    
    def test_find_minimum_difference_goodies_case3(self):
        # Test Case 3: Larger number of employees (6)
        goodies = {
            "Fitbit Plus": 7980,
            "IPods": 22349,
            "MI Band": 999,
            "Cult Pass": 2799,
            "Macbook Pro": 229900,
            "Digital Camera": 11101,
            "Alexa": 9999,
            "Sandwich Toaster": 2195,
            "Microwave Oven": 9800,
            "Scale": 4999
        }
        num_employees = 6
        
        expected_goodies = [
            ("Sandwich Toaster", 2195),
            ("Cult Pass", 2799),
            ("Scale", 4999),
            ("Fitbit Plus", 7980),
            ("Microwave Oven", 9800),
            ("Alexa", 9999)
        ]
        expected_diff = 7804
        
        sorted_goodies = sort_goodies_by_price(goodies)
        selected_goodies, min_diff = find_minimum_difference_goodies(sorted_goodies, num_employees)
        
        self.assertEqual(selected_goodies, expected_goodies)
        self.assertEqual(min_diff, expected_diff)

    def test_find_minimum_difference_goodies_case4(self):
        # Test Case 4: Only one employee
        goodies = {
            "Fitbit Plus": 7980,
            "Alexa": 9999,
            "Sandwich Toaster": 2195
        }
        num_employees = 1
        
        expected_goodies = [("Sandwich Toaster", 2195)]
        expected_diff = 0
        
        sorted_goodies = sort_goodies_by_price(goodies)
        selected_goodies, min_diff = find_minimum_difference_goodies(sorted_goodies, num_employees)
        
        self.assertEqual(selected_goodies, expected_goodies)
        self.assertEqual(min_diff, expected_diff)

    def test_find_minimum_difference_goodies_case5(self):
        # Test Case 5: All items have the same price
        goodies = {
            "Fitbit Plus": 5000,
            "IPods": 5000,
            "MI Band": 5000,
            "Cult Pass": 5000
        }
        num_employees = 3
        
        expected_goodies = [
            ("Fitbit Plus", 5000),
            ("IPods", 5000),
            ("MI Band", 5000)
        ]
        expected_diff = 0
        
        sorted_goodies = sort_goodies_by_price(goodies)
        selected_goodies, min_diff = find_minimum_difference_goodies(sorted_goodies, num_employees)
        
        self.assertEqual(selected_goodies, expected_goodies)
        self.assertEqual(min_diff, expected_diff)

if __name__ == "__main__":
    unittest.main()
