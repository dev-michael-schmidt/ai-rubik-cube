import numpy as np

class RubikCube:
    """
    Hello.  I am a docstring.
    """

    def __init__(self):
        self.cube = [[' ' for _ in range(12)] for _ in range(9)]
        self.cube = np.array(self.cube)
        for r_idx in range(3):
            for c_idx in range(3, 6):
                self.cube[r_idx][c_idx] = 'W'

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
            for c in range(3, 6):
                self.cube[r][c] = 'O'

    def __str__(self):
        res = ''
        for r_idx in range(9):
            row = self.cube[r_idx][0]
            for c_idx in range(1, 12):
                row = '{} {}'.format(row, self.cube[r_idx][c_idx])

            if r_idx:
                res = '{}\n{}'.format(res, row)
            else:
                res = row

        return res

    def y_rotate(self, slot, direction):
        """

        :slot:  str     left, right
        :dir:   str     up, down
        """

        if slot not in ('left', 'right'):
            raise

        if direction not in ('up', 'down'):
            raise

        temp = [] # IDEA: using np slicing below ??
        col = 3 if slot == 'left' else 5
        anti_col = 14 - col

        # NOTE: probably a bug on rotations for right most group on 3x6 and 9x12 (np.rot90)??

        temp = [self.cube[r_idx][col] for r_idx in range(9)]
        for r_idx in range(3, 6):
            temp.append(self.cube[r_idx][anti_col])

        temp = temp[3:] + temp[:3] if direction == 'up' else temp[-3:] + temp[:-3]

        for r_idx in range(9):
            self.cube[r_idx][col] = temp[r_idx]

        for r_idx in range(3, 6):
            self.cube[r_idx][anti_col] = temp[r_idx + 6]

        if slot == 'left':
            self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3])
            if direction == 'down':
                self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3], k=2)
        elif slot == 'right':
            self.cube[3:6, 6:9] = np.rot90(self.cube[3:6, 6:9])
            if direction == 'up':
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

        if slot == 'front':
            if dir == 'clockwise':
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

            temp = np.rot90(temp, k=3) if dir == 'clockwise' else np.rot90(temp)

            self.cube[3:6, 8:12] = temp[1:4, :4]
            self.cube[8, 3:6] = np.flip(temp[4, 1:4])
            self.cube[3:6, 0] = temp[1:4, 4]
            self.cube[0, 3:6] = np.flip(temp[0, 1:4])

    def heuristic1(self):
        """
        For each cubie, compute the minimum number of moves required to
        correctly position and orient it, and sum these values over all cubies.
        Unfortunately, to be admissible, this value has to be divided by 8,
        since every twist moves 8 cubies.
        """
        pass

    def heuristic2(self):
        """
        A better heuristic is to take the maximum of the sum of Manhattan
        distances of the corner cubies, divided by four, and the maximum of the
        sum of edge cubies divided by 4.
        """
        pass
