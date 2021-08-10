
import unittest
import context
from colorname import get_color_name # pylint: disable=import-error

class TestGetColorName(unittest.TestCase):

    def test_gets_red(self):
        cases = [
            (102, 0,   0),
            (153, 0,   0),
            (204, 0,   0),
            (255, 0,   0),
            (255, 51,  51),
            (255, 102, 102),
            (255, 153, 153),
            (255, 204, 204),
        ]
        for case in cases:
            expected = 'red'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


    def test_gets_green(self):
        cases = [
            (0,   102, 0),
            (0,   153, 0),
            (0,   204, 0),
            (0,   255, 0),
            (51,  255, 51),
            (102, 255, 102),
            (153, 255, 153),
            (204, 255, 204),
        ]
        for case in cases:
            expected = 'green'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


    def test_gets_blue(self):
        cases = [
            (0,   0,   102),
            (0,   0,   153),
            (0,   0,   204),
            (0,   0,   255),
            (51,  51,  255),
            (102, 102, 255),
            (153, 153, 255),
            (204, 204, 255),
        ]
        for case in cases:
            expected = 'blue'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


    def test_gets_yellow(self):
        cases = [
            (102, 102, 0),
            (153, 153, 0),
            (204, 204, 0),
            (255, 255, 0),
            (255, 255, 51),
            (255, 255, 102),
            (255, 255, 153),
            (255, 255, 204),
        ]
        for case in cases:
            expected = 'yellow'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


    def test_gets_cyan(self):
        cases = [
            (0,   153, 153),
            (0,   102, 102),
            (0,   204, 204),
            (0,   255, 255),
            (51,  255, 255),
            (102, 255, 255),
            (153, 255, 255),
            (204, 255, 255),
        ]
        for case in cases:
            expected = 'cyan'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


    def test_gets_magenta(self):
        cases = [
            (102, 0,   102),
            (153, 0,   153),
            (204, 0,   204),
            (255, 0,   255),
            (255, 51,  255),
            (255, 102, 255),
            (255, 153, 255),
            (255, 204, 255),
        ]
        for case in cases:
            expected = 'magenta'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


    def test_gets_white(self):
        cases = [
            (255, 221, 221),
            (221, 255, 221),
            (221, 221, 255),
            (255, 255, 221),
            (221, 255, 255),
            (255, 221, 255),
            (255, 255, 255),
        ]
        for case in cases:
            expected = 'white'
            actual = get_color_name(*case)
            msg = f'actual result for {case} was {actual}, expected {expected}'
            self.assertEqual(actual, expected, msg=msg)


if __name__ == '__main__':
    unittest.main()
