import unittest

from src.high_scores import high_to_low, latest, personal_best, personal_top_three


class HighScoresTest(unittest.TestCase):

    def test_latest_score(self):
        self.assertEqual(100, latest([50, 55, 65, 100]))

    def test_personal_best(self):
        self.assertEqual(500, personal_best([100, 200, 300, 500]))

    def test_personal_top_three(self):
        self.assertEqual([5, 4, 3], personal_top_three([1, 2, 3, 4, 5]))

    def test_high_to_low(self):
        self.assertEqual([5, 4, 3, 2, 1], high_to_low([1, 2, 3, 4, 5]))

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
