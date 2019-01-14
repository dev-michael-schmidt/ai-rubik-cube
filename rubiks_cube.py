import numpy as np
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

    def vertical_rotate(self, slot, dir):
        """

        :slot:  str     left, middle, right
        :dir:   str     up, down
        """

        if slot != 'left' and slot != 'middle' and slot != 'right':
            raise

        if dir != 'up' and dir != 'down':
            raise

        temp = []
        c = 3 if slot == 'left' else 4 if slot == 'middle' else 5
        anti_c = 14 - c

        temp = [self.cube[r][c] for r in range(9)]
        for r in range(3, 6):
            temp.append(self.cube[r][anti_c])

        temp = temp[3:] + temp[:3] if dir == 'up' else temp[-3:] + temp[:-3]

        for r in range(9):
            self.cube[r][c] = temp[r]

        for r in range(3, 6):
            self.cube[r][anti_c] = temp[r + 6]

        self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3])
        if dir == 'down':
            for _ in range(2):
                self.cube[3:6, 0:3] = np.rot90(self.cube[3:6, 0:3])

    def horizontal_rotate(self, slot):
        pass
