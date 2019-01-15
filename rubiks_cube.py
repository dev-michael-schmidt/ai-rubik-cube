import numpy as np
from termcolor import colored

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class RubiksCube:

    def __init__(self):
        self.cube = [['.' for _ in range(12)] for _ in range(9)]
        self.cube = np.array(self.cube)
        for r in range(3):
            for c in range(3):
                self.cube[r][c] = ' '

            for c in range(3, 6):
                self.cube[r][c] = 'W'

            for c in range(6, 12):
                self.cube[r][c] = ' '

        for r in range(3, 6):
            for c in range(3):
                self.cube[r][c] = 'R'

            for c in range(3, 6):
                self.cube[r][c] = 'B'

            for c in range(6, 9):
                self.cube[r][c] = 'G'

            for c in range(9, 12):
                self.cube[r][c] = 'Y'

        for r in range(6, 9):
            for c in range(3):
                self.cube[r][c] = ' '

            for c in range(3, 6):
                self.cube[r][c] = 'O'

            for c in range(6, 12):
                self.cube[r][c] = ' '

    def __str__(self):
        s = ''
        for r in range(9):
            row = self.cube[r][0]
            for c in range(1, 12):
                row = '{} {}'.format(row, self.cube[r][c])

            if r == 0:
                s = row
            else:
                s = '{}\n{}'.format(s, row)

        return s

    def y_rotate(self, slot, dir):
        """

        :slot:  str     left, right
        :dir:   str     up, down
        """

        if slot != 'left' and slot != 'right':
            raise

        if dir != 'up' and dir != 'down':
            raise

        temp = [] # IDEA: using np slicing below ??
        c = 3 if slot == 'left' else 5
        anti_c = 14 - c

        # NOTE: probably a bug on rotations for right most group on 3x6 and 9x12 (np.rot90)??

        temp = [self.cube[r][c] for r in range(9)]
        for r in range(3, 6):
            temp.append(self.cube[r][anti_c])

        temp = temp[3:] + temp[:3] if dir == 'up' else temp[-3:] + temp[:-3]

        for r in range(9):
            self.cube[r][c] = temp[r]

        for r in range(3, 6):
            self.cube[r][anti_c] = temp[r + 6]

        if slot == 'left':
            self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3])
            if dir == 'down':
                self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3], k=2)
        elif slot == 'right':
            self.cube[3:6, 6:9] = np.rot90(self.cube[3:6, 6:9])
            if dir == 'up':
                self.cube[3:6, 6:9] = np.rot90(self.cube[3:6, 6:9], k=2)

    def x_rotate(self, slot, dir):
        """

        """
        if slot != 'top' and slot != 'bottom':
            raise

        if dir != 'left' and dir != 'right':
            raise

        r = 3 if slot == 'top' else 4 if slot == 'middle' else 5
        c = -3 if dir == 'right' else 3
        self.cube[r, :] = np.concatenate((self.cube[r, c:], self.cube[r, :c]))

        if slot == 'top':
            if dir == 'left':
                self.cube[0:3, 3:6] = np.rot90(self.cube[0:3, 3:6], k=3)
            else:
                self.cube[0:3, 3:6] = np.rot90(self.cube[0:3, 3:6])
        elif slot == 'bottom':
            if dir == 'left':
                self.cube[6:9, 3:6] = np.rot90(self.cube[6:9, 3:6])
            else:
                self.cube[6:9, 3:6] = np.rot90(self.cube[6:9, 3:6], k=3)

    def z_rotate(self, slot, dir):
        """

        """
        if slot != 'front' and slot != 'back':
            raise

        if dir != 'clockwise' and dir != 'anti-clockwise':
            raise

        edges = [
            np.array(self.cube[2, 3:6]), np.array(self.cube[3:6, 6]),
            np.array(self.cube[6, 3:6]), np.array(self.cube[3:6, 2])
        ]

        if slot == 'front':
            if dir == 'clockwise':
                self.cube[2, 3:6] = np.flip(edges[3])
                self.cube[3:6, 6] = edges[0]
                self.cube[6, 3:6] = np.flip(edges[1])
                self.cube[3:6, 2] = edges[2]
                self.cube[3:6, 3:6] = np.rot90(self.cube[3:6, 3:6], k=3)
