from unittest import TestCase

from Grid import Grid
from Robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        grid = Grid()  # based on 5x5 grid
        self.robot = Robot(grid)
        self.DIRECTION = ('NORTH', 'SOUTH', 'EAST', 'WEST')

    def test_move(self):
        self.robot.place(5,5, 'NORTH')
        self.assertEqual(self.robot.move(), False)
        self.robot.place(5,5, 'EAST')
        self.assertEqual(self.robot.move(), False)
        self.robot.place(5,5, 'SOUTH')
        self.assertEqual(self.robot.move(), True)
        self.robot.place(5,5, 'WEST')
        self.assertEqual(self.robot.move(), True)

        self.robot.place(0,0, 'NORTH')
        self.assertEqual(self.robot.move(), True)
        self.robot.place(0,0, 'EAST')
        self.assertEqual(self.robot.move(), True)
        self.robot.place(0,0, 'SOUTH')
        self.assertEqual(self.robot.move(), False)
        self.robot.place(0,0, 'WEST')
        self.assertEqual(self.robot.move(), False)


    def test_turn(self):
        self.assertEqual(self.robot.turn('left'), False)
        self.assertEqual(self.robot.turn('right'), False)
        self.assertEqual(self.robot.turn(2j), False)
        self.assertEqual(self.robot.turn(object), False)
        self.assertEqual(self.robot.turn({}), False)
        self.assertEqual(self.robot.turn([]), False)

        self.assertIn(self.robot.turn('RIGHT'), self.DIRECTION)
        self.assertIn(self.robot.turn('LEFT'), self.DIRECTION)

    def test_place(self):
        self.assertEqual(self.robot.place(1, 1), True)
        self.assertEqual(self.robot.place(0, 0), True)
        self.assertEqual(self.robot.place(5, 5), True)
        self.assertEqual(self.robot.place(-1, -1), False)
        self.assertEqual(self.robot.place("1", "1"), True)
        self.assertEqual(self.robot.place(6, 6), False)
        self.assertEqual(self.robot.place(6, 1), False)
        self.assertEqual(self.robot.place(1, 6), False)
        self.assertEqual(self.robot.place(3, 3, 'NORTH'), True)
        self.assertEqual(self.robot.place(3, 3, 'north'), False)
        self.assertEqual(self.robot.place(3, 3, 'SOUTH'), True)
        self.assertEqual(self.robot.place(3, 3, 'test'), False)
        self.assertEqual(self.robot.place(3, 6, 'NORTH'), False)

        self.assertRaises(TypeError, self.robot.place, 2j)
        self.assertRaises(TypeError, self.robot.place, object)
        self.assertRaises(TypeError, self.robot.place, {})
        self.assertRaises(TypeError, self.robot.place, [])
