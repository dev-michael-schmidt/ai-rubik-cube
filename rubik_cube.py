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

        for _r in range(3, 6):
            for _c in range(3):
                self.cube[_r][_c] = 'R'

            for _c in range(3, 6):
                self.cube[_r][_c] = 'B'

            for _c in range(6, 9):
                self.cube[_r][_c] = 'G'

            for _c in range(9, 12):
                self.cube[_r][_c] = 'Y'

        for _r in range(6, 9):
            for _c in range(3, 6):
                self.cube[_r][_c] = 'O'

    def __str__(self):
        res = ''
        for _r in range(9):
            row = self.cube[_r][0]
            for _c in range(1, 12):
                row = '{} {}'.format(row, self.cube[_r][_c])

            res = '{}\n{}'.format(res, row) if _r else row

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

    def x_rotate(self, slot, direction):
        """
        I am a docstring.
        """
        if slot not in ('top', 'bottom'):
            raise

        if direction not in ('left', 'right'):
            raise

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

    def z_rotate(self, slot, direction):
        """
        I am a docstring.
        """

        if slot not in ('front', 'back'):
            raise

        if direction not in ('clockwise', 'anti-clockwise'):
            raise

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

            temp = np.rot90(temp, k=3) if direction == 'clockwise' else np.rot90(temp)

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
        return self

    def heuristic2(self):
        """
        A better heuristic is to take the maximum of the sum of Manhattan
        distances of the corner cubies, divided by four, and the maximum of the
        sum of edge cubies divided by 4.
        """
        return self
