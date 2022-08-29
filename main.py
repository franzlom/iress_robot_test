from dataclasses import dataclass
from Grid import Grid

from Robot import Robot

ALLOWED_COMMANDS = ('MOVE', 'LEFT', 'RIGHT', 'REPORT', 'PLACE')


def check_robot_exist(robot_object):
    if not robot_object:
        print('Place Robot First!')
        return False
    else:
        if isinstance(robot_object, Robot):
            return True
        raise TypeError


if __name__ == '__main__':
    print('Hi Welcome to Franz Robot Code for Iress. Start by Saying PlACE')
    grid = Grid()
    robot = None

    # main thread
    while True:
        print('Waiting Input...')
        user_input = input()
        user_input = user_input.split(' ')
        if not user_input[0] in ALLOWED_COMMANDS:
            print('Unrecognised command, please try again.')
            continue
        if user_input[0] in ALLOWED_COMMANDS:
            match user_input[0]:
                case 'PLACE':
                    input_length = len(user_input)
                    if input_length == 2:
                        starting_info = user_input[-1].split(',')
                        if len(starting_info) != 3:
                            print(f'I did not understand the commands after PLACE "{starting_info}"')
                            continue
                        x, y, f = starting_info
                        robot = Robot(grid)
                        if robot.place(x, y, f):
                            continue
                        else:
                            del robot
                    else:
                        robot = Robot(grid)
                        robot.place(0, 0)
                case 'MOVE':
                    if check_robot_exist(robot):
                        robot.move()
                case 'LEFT':
                    if check_robot_exist(robot):
                        robot.turn(user_input[0])
                case 'RIGHT':
                    if check_robot_exist(robot):
                        robot.turn(user_input[0])
                case 'REPORT':
                    if check_robot_exist(robot):
                        robot.report()
                case _:
                    print(f'Unrecognised command "{user_input[0]}"')

