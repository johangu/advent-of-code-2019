import unittest

from day02 import part01


class TestDay02(unittest.TestCase):

    def test_part01(self):
        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
                         part01([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))
        self.assertEqual([2, 0, 0, 0, 99], part01([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], part01([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801], part01([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99],
                         part01([1, 1, 1, 4, 2, 5, 6, 0, 99]))


if __name__ == '__main__':
    unittest.main()
