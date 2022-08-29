from unittest import TestCase
from Grid import Grid


class TestGrid(TestCase):

    def setUp(self) -> None:
        self.grid = Grid()

    def test_valid_x(self):
        self.assertEqual(self.grid.valid_x(-1), False)
        self.assertEqual(self.grid.valid_x(0), True)
        self.assertEqual(self.grid.valid_x(1), True)
        self.assertEqual(self.grid.valid_x(5), True)
        self.assertEqual(self.grid.valid_x(6), False)
        self.assertEqual(self.grid.valid_x("1"), True)

        self.assertRaises(TypeError, self.grid.valid_x, 2j)
        self.assertRaises(TypeError, self.grid.valid_x, object)
        self.assertRaises(TypeError, self.grid.valid_y, {})
        self.assertRaises(TypeError, self.grid.valid_y, [])


    def test_valid_y(self):
        self.assertEqual(self.grid.valid_y(-1), False)
        self.assertEqual(self.grid.valid_y(0), True)
        self.assertEqual(self.grid.valid_y(1), True)
        self.assertEqual(self.grid.valid_y(5), True)
        self.assertEqual(self.grid.valid_y(6), False)
        self.assertEqual(self.grid.valid_y("1"), True)

        self.assertRaises(TypeError, self.grid.valid_y, 2j)
        self.assertRaises(TypeError, self.grid.valid_y, object)
        self.assertRaises(TypeError, self.grid.valid_y, {})
        self.assertRaises(TypeError, self.grid.valid_y, [])

    def test_valid_position(self):
        self.assertEqual(self.grid.valid_position(1,1), True)
        self.assertEqual(self.grid.valid_position(2,1), True)
        self.assertEqual(self.grid.valid_position(5,5), True)
        self.assertEqual(self.grid.valid_position(0,0), True)
        self.assertEqual(self.grid.valid_position(6,6), False)
        self.assertEqual(self.grid.valid_position(6,1), False)
        self.assertEqual(self.grid.valid_position("1","1"), True)
        self.assertEqual(self.grid.valid_position("6","1"), False)

        self.assertRaises(TypeError, self.grid.valid_y, 2j)
        self.assertRaises(TypeError, self.grid.valid_y, object)
        self.assertRaises(TypeError, self.grid.valid_y, {})
        self.assertRaises(TypeError, self.grid.valid_y, [])






