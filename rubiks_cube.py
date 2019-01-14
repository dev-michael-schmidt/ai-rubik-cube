class RubiksCube:

    def __init__(self):
        self.cube = [['.' for _ in range(12)] for _ in range(9)]
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
