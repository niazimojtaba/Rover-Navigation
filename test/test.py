import sys
import unittest

from io import StringIO
from rover import RoverRoute, StreamingInputOutput


def set_up(input):
    stream = StreamingInputOutput(StringIO(input))
    first_position = stream.read().split()
    x, y, rotation = first_position
    plateau = RoverRoute(x, y, rotation, 5, 5)
    movements = stream.read().split()
    for rotate_or_move in movements:
        plateau.update(rotate_or_move)
    return plateau


class TestRoverRoute(unittest.TestCase):

    def test_first_testcase(self):
        input = """1 2 N
L M L M L M L M M
"""
        plateau = set_up(input)
        self.assertEqual(1, plateau.x)
        self.assertEqual(3, plateau.y)
        self.assertEqual('N', plateau.rotation)

    def test_second_testcase(self):
        input = """3 3 E
M M R M M R M R R M
"""
        plateau = set_up(input)
        self.assertEqual(5, plateau.x)
        self.assertEqual(1, plateau.y)
        self.assertEqual('E', plateau.rotation)

    def test_cycle_r(self):
        input = """3 3 E
R R R R
"""
        plateau = set_up(input)
        self.assertEqual(3, plateau.x)
        self.assertEqual(3, plateau.y)
        self.assertEqual('E', plateau.rotation)

    def test_cycle_l(self):
        input = """3 3 E
L L L L
"""
        plateau = set_up(input)
        self.assertEqual(3, plateau.x)
        self.assertEqual(3, plateau.y)
        self.assertEqual('E', plateau.rotation)

    def test_down(self):
        input = """3 3 N
L L M
"""
        plateau = set_up(input)
        self.assertEqual(3, plateau.x)
        self.assertEqual(2, plateau.y)
        self.assertEqual('S', plateau.rotation)


if __name__ == "__main__":
    unittest.main()