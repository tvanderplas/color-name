
import unittest
import context
from colorname import get_color_name # pylint: disable=import-error

class TestGetColorName(unittest.TestCase):
    
    def test_gets_red(self):
        cases = [
            (102, 0, 0),
            (153, 0, 0),
            (204, 0, 0),
            (255, 0, 0),
            (255, 51, 51),
            (255, 102, 102),
            (255, 153, 153),
            (255, 204, 204),
        ]
        for case in cases:
            expected = 'red'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


if __name__ == '__main__':
    unittest.main()
