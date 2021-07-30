
import unittest
import context
from colorname import get_color_name # pylint: disable=import-error

class TestGetColorName(unittest.TestCase):
    
    def test_gets_red(self):
        cases = [
            (255, 0, 0),
        ]
        for case in cases:
            self.assertEqual(get_color_name(*case), 'red')


if __name__ == '__main__':
    unittest.main()
