import unittest
from job_schedule import job_scheduling

class TestJobScheduling(unittest.TestCase):

    def test_case_1(self):
        input_data = """
        0900
        1030
        100
        1000
        1200
        500
        1100
        1200
        300
        """
        expected_output = [2, 400]
        self.assertEqual(job_scheduling(input_data), expected_output)

    def test_case_2(self):
        input_data = """
        0900
        1000
        250
        0945
        1200
        550
        1130
        1500
        150
        """
        expected_output = [2, 400]
        self.assertEqual(job_scheduling(input_data), expected_output)

    def test_case_3(self):
        input_data = """
        0900
        1030
        100
        1000
        1200
        100
        1100
        1200
        100
        """
        expected_output = [1, 100]
        self.assertEqual(job_scheduling(input_data), expected_output)

    def test_case_4(self):
        input_data = """
        0900
        1100
        200
        1030
        1200
        300
        1100
        1300
        250
        """
        expected_output = [2, 450]
        self.assertEqual(job_scheduling(input_data), expected_output)

    def test_case_5(self):
        input_data = """
        0900
        1000
        1000
        1000
        1100
        200
        1100
        1200
        150
        """
        expected_output = [0, 0]
        self.assertEqual(job_scheduling(input_data), expected_output)

    def test_case_6(self):
        input_data = """
        0900
        0930
        50
        0930
        1000
        70
        1000
        1100
        90
        1100
        1200
        110
        """
        expected_output = [3, 210]
        self.assertEqual(job_scheduling(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
