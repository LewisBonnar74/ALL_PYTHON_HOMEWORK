import unittest

from src.high_scores import latest, personal_best, personal_top_three


class HighScoresTest(unittest.TestCase):

    def test_latest_score(self):
        self.assertEqual(100, latest([50, 55, 65, 100]))

    def test_personal_best(self):
        self.assertEqual(500, personal_best([100, 200, 300, 500]))

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
