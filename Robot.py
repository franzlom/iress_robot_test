import random
from dataclasses import dataclass
from Grid import Grid

DIRECTION = ('NORTH', 'SOUTH', 'EAST', 'WEST')

TURN_LEFT = 'LEFT'
TURN_RIGHT = 'RIGHT'


@dataclass
class Robot:
    grid: Grid
    __x: int = 0
    __y: int = 0
    __direction: str = random.choice(DIRECTION)

    def move(self):
        new_y = None
        new_x = None
        match self.__direction:
            case 'NORTH':
                new_y = self.__y + 1
            case 'SOUTH':
                new_y = self.__y - 1
            case 'EAST':
                new_x = self.__x + 1
            case 'WEST':
                new_x = self.__x - 1
        if new_y or new_y == 0:
            if self.grid.valid_y(new_y):
                self.__y = new_y
            else:
                print('Woah there partner, you are about to fall off the board!')
                return False
        elif new_x or new_x == 0:
            if self.grid.valid_x(new_x):
                self.__x = new_x
            else:
                print('Woah there partner, you are about to fall off the board!')
                return False
        self.report()
        return True

    def turn(self, turn_command):
        if turn_command not in (TURN_LEFT, TURN_RIGHT):
            print(f'"{turn_command}"is not recognised. Use {TURN_LEFT} or {TURN_RIGHT}')
            return False

        match self.__direction:
            case 'NORTH':
                if turn_command == TURN_LEFT:
                    self.__direction = 'WEST'
                elif turn_command == TURN_RIGHT:
                    self.__direction = 'EAST'
            case 'SOUTH':
                if turn_command == TURN_LEFT:
                    self.__direction = 'EAST'
                elif turn_command == TURN_RIGHT:
                    self.__direction = 'WEST'
            case 'EAST':
                if turn_command == TURN_LEFT:
                    self.__direction = 'NORTH'
                elif turn_command == TURN_RIGHT:
                    self.__direction = 'SOUTH'
            case 'WEST':
                if turn_command == TURN_LEFT:
                    self.__direction = 'SOUTH'
                elif turn_command == TURN_RIGHT:
                    self.__direction = 'NORTH'
        self.report()
        return self.__direction

    def place(self, new_x, new_y, direction=None):
        if self.grid.valid_position(new_x, new_y) and (direction in DIRECTION + (None,)):
            self.__x = new_x
            self.__y = new_y
            self.__direction = direction if direction else random.choice(DIRECTION)
            self.report()
            return True
        else:
            print(f'Could not place the bot with "{new_x}" and "{new_y}" position with direction "{direction}"')
            return False

    def report(self):
        print(f'I am at position {self.__x}x {self.__y}y and facing {self.__direction}')
