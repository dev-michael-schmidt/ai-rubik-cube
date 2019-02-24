"""
I am a doc docstring
"""

import random
import numpy as np

class Cubie:
    """

    """
    def __init__(self):
        pass


class RubikCube:
    """
    Hello.  I am a docstring.
    """

    def __init__(self):
        self.cube = [[' ' for _ in range(12)] for _ in range(9)]
        self.cube = np.array(self.cube)

        self.colors = ('W', 'G', 'R', 'B', 'O', 'Y')

        for _r in range(3):
            for _c in range(3, 6):
                self.cube[_r][_c] = self.colors[0]

        for _r in range(3, 6):
            for _c in range(3):
                self.cube[_r][_c] = self.colors[1]

            for _c in range(3, 6):
                self.cube[_r][_c] = self.colors[2]

            for _c in range(6, 9):
                self.cube[_r][_c] = self.colors[3]

            for _c in range(9, 12):
                self.cube[_r][_c] = self.colors[4]

        for _r in range(6, 9):
            for _c in range(3, 6):
                self.cube[_r][_c] = self.colors[5]

    def __str__(self):
        res = ''
        for _r in range(9):
            row = self.cube[_r][0]
            for _c in range(1, 12):
                row = '{} {}'.format(row, self.cube[_r][_c])

            res = '{}\n{}'.format(res, row) if _r else row

        return res

    def __repr__(self):

        return str(self)

    def scramble(self, moves=10000):
        """
        Scramble a cube by randomly rotating sides using built-in rotate methods

        :moves:     int     (Optional)  The number of roations to perform
        """
        rot_functions = {
            0: self.x_rotate,
            1: self.y_rotate,
            2: self.z_rotate}

        params = {
            0: ['top', 'left'],
            1: ['top', 'right'],
            2: ['bottom', 'left'],
            3: ['bottom', 'right'],
            4: ['left', 'up'],
            5: ['left', 'down'],
            6: ['right', 'up'],
            7: ['right', 'down'],
            8: ['front', 'clockwise'],
            9: ['front', 'anti-clockwise'],
            10: ['back', 'clockwise'],
            11: ['back', 'anti-clockwise']}

        actions = [random.randint(0, len(rot_functions) - 1) for _ in range(moves)]
        args = [actions[i] * 4 + random.randint(0, 3) for i in range(moves)]

        rotations = [rot_functions[i] for i in actions]
        slots = [params[args[i]][0] for i in range(moves)]
        directions = [params[args[i]][1] for i in range(moves)]

        for rotation, slot, direction in zip(rotations, slots, directions):
            rotation(slot, direction)

    def x_rotate(self, slot, direction):
        """
        I am a docstring.
        """

        if slot not in {'top', 'bottom'}:
            raise ValueError('slot arg must be top/bottom, not `{}`'.format(slot))

        if direction not in {'left', 'right'}:
            raise ValueError('direction arg must be left/right, not `{}`'.format(direction))

        _r = 3 if slot == 'top' else 4 if slot == 'middle' else 5
        _c = -3 if direction == 'right' else 3
        self.cube[_r, :] = np.concatenate((self.cube[_r, _c:], self.cube[_r, :_c]))

        if slot == 'top':
            if direction == 'left':
                self.cube[0:3, 3:6] = np.rot90(self.cube[0:3, 3:6], k=3)
            else:
                self.cube[0:3, 3:6] = np.rot90(self.cube[0:3, 3:6])
        else:
            if direction == 'left':
                self.cube[6:9, 3:6] = np.rot90(self.cube[6:9, 3:6])
            else:
                self.cube[6:9, 3:6] = np.rot90(self.cube[6:9, 3:6], k=3)

    def y_rotate(self, slot, direction):
        """

        :slot:  str     left, right
        :dir:   str     up, down
        """

        if slot not in {'left', 'right'}:
            raise ValueError('slot arg must be left/right, not `{}`'.format(slot))

        if direction not in {'up', 'down'}:
            raise ValueError('direction arg must be up/down, not `{}`'.format(direction))

        temp = [] # IDEA: using np slicing below ??
        col = 3 if slot == 'left' else 5
        anti_col = 14 - col

        # NOTE: probably a bug on rotations for right most group on 3x6 and 9x12 (np.rot90)??

        temp = [self.cube[_r][col] for _r in range(9)]
        for _r in range(3, 6):
            temp.append(self.cube[_r][anti_col])

        temp = temp[3:] + temp[:3] if direction == 'up' else temp[-3:] + temp[:-3]

        for _r in range(9):
            self.cube[_r][col] = temp[_r]

        for _r in range(3, 6):
            self.cube[_r][anti_col] = temp[_r + 6]

        if slot == 'left':
            self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3])
            if direction == 'down':
                self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3], k=2)
        elif slot == 'right':
            self.cube[3:6, 6:9] = np.rot90(self.cube[3:6, 6:9])
            if direction == 'up':
                self.cube[3:6, 6:9] = np.rot90(self.cube[3:6, 6:9], k=2)

    def z_rotate(self, slot, direction):
        """
        I am a docstring.
        """
        if slot not in {'front', 'back'}:
            raise ValueError('slot arg must be front/back, not `{}`'.format(slot))

        if direction not in {'clockwise', 'anti-clockwise'}:
            raise ValueError('direction arg must be clockwise/anti-clockwise, not `{}`'.format(direction))

        if slot == 'front':
            if direction == 'clockwise':
                self.cube[2:7, 2:7] = np.rot90(self.cube[2:7, 2:7], k=3)
            else:
                self.cube[2:7, 2:7] = np.rot90(self.cube[2:7, 2:7])
        else:
            # no copy, refence?
            temp = np.array([[' ' for _ in range(5)] for _ in range(5)])
            temp[1:4, :4] = np.array(self.cube[3:6, 8:12])
            temp[0, 1:4] = np.array(np.flip(self.cube[0, 3:6]))
            temp[1:4, 4] = np.array(self.cube[3:6, 0])
            temp[4, 1:4] = np.array(np.flip(self.cube[8, 3:6]))

            temp = np.rot90(temp, k=3) if direction == 'anti-clockwise' else np.rot90(temp)

            self.cube[3:6, 8:12] = temp[1:4, :4]
            self.cube[8, 3:6] = np.flip(temp[4, 1:4])
            self.cube[3:6, 0] = temp[1:4, 4]
            self.cube[0, 3:6] = np.flip(temp[0, 1:4])

    def heuristic1(self):
        """
        For each cubie, compute the minimum number of moves required to correctly position and
        orient it, and sum these values over all cubies. Unfortunately, to be admissible, this value
        has to be divided by 8, since every twist moves 8 cubies.
        """

        moves = 0

        for row, col in [(0, 3), (0, 5), (2, 5), (2, 3)]:
            if self.cube[row][col] != 'W':
                moves += 2 / 8 if self.cube[row][col] == 'Y' else 1 / 8

        for row, col in [(1, 3), (1, 5)]:
            if self.cube[row][col] != 'W':
                moves += 1 / 8 if self.cube[row][col] in ('R', 'O') else 2 / 8

        for row, col in [(0, 4), (2, 4)]:
            if self.cube[row][col] != 'W':
                moves += 1 / 8 if self.cube[row][col] in ('B', 'G') else 2 / 8

        for row, col in [(6, 3), (6, 5), (8, 5), (8, 3)]:
            if self.cube[row][col] != 'Y':
                moves += 2 / 8 if self.cube[row][col] == 'W' else 1 / 8

        for row, col in [(7, 3), (7, 5)]:
            if self.cube[row][col] != 'Y':
                moves += 1 / 8 if self.cube[row][col] in ('R', 'O') else 2 / 8

        for row, col in [(6, 4), (8, 4)]:
            if self.cube[row][col] != 'Y':
                moves += 1 / 8 if self.cube[row][col] in ('B', 'G') else 2 / 8

        for row, col in [(4, 6), (4, 8)]:
            if self.cube[row][col] != 'B':
                moves += 1 / 8 if self.cube[row][col] in ('W', 'Y') else 2 / 8

        for row, col in [(4, 0), (4, 2)]:
            if self.cube[row][col] != 'G':
                moves += 1 / 8 if self.cube[row][col] in ('W', 'Y') else 2 / 8

        return moves


    def heuristic2(self):
        """
        A better heuristic is to take the maximum of the sum of Manhattan
        distances of the corner cubies, divided by four, and the maximum of the
        sum of edge cubies divided by 4.

                    W
                R   B   G   Y
                    O
        """
        return self
