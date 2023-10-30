####################################################
#
# run_test.py
#
# Unit tests for run.py
#
# GVSU CIS 500
#
#####################################################

import unittest
import run

class WordleEngineTest(unittest.TestCase):

    def test_constructor_sets_distance(self):
        r = run.Run("1:00", "1:05", 1.2)
        self.assertEqual(1.2, r.distance)

    def test_constructor_sets_raw_start(self):
        r = run.Run("1:05", "2:10", 5)
        self.assertEqual(65, r.raw_start)

    def test_constructor_sets_raw_end(self):
        r = run.Run("1:05", "15:17", 5)
        self.assertEqual(15*60+17, r.raw_end) 

    def test_elapsed_minutes1(self):
        r = run.Run("11:15", "14:43", 6.2)
        self.assertEqual(208, r.elapsed_minutes())

    def test_elapsed_minutes2(self):
        r = run.Run("11:43", "14:15", 6.2)
        self.assertEqual(152, r.elapsed_minutes())   

    def test_elapsed_time1(self):
        r = run.Run("11:15", "14:43", 6.2)
        self.assertEqual("3:28", r.elapsed_time())

    def test_elapsed_time2(self):
        r = run.Run("11:43", "14:15", 6.2)
        self.assertEqual("2:32", r.elapsed_time())  

    def test_raw_pace1(self):
        r = run.Run("12:00", "12:10", 1.0)
        self.assertEqual(10, r.raw_pace())

    def test_raw_pace2(self):
        r = run.Run("12:00", "12:25", 2.5)
        self.assertEqual(10, r.raw_pace())

    def test_raw_pace3(self):
        r = run.Run("8:00", "10:09", 26.2)
        self.assertAlmostEqual(4.9236641, r.raw_pace(), 4)

    def test_pace1(self):
        r = run.Run("12:00", "12:21", 2)
        self.assertEqual("10:30/km")

    def test_pace1(self):
        run.Run.unit = "mile"
        r = run.Run("8:00", "10:09", 26.2)
        self.assertEqual("4:55/mile", r.pace())

    def test_str(self):
        run.Run.unit = "mile"
        r = run.Run("8:00", "10:09", 26.2)
        self.assertEqual("26.2 miles in 2:09. Pace: 4:55/mile.", r.__str__())


# This bit of "magic" lets you run the tests from the command line by 
# running "python run_test.py"
if __name__ == '__main__':
    unittest.main()