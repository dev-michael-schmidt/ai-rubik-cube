from rubiks_cube import RubiksCube

r = RubiksCube()


r.y_rotate('left', 'down')
r.y_rotate('right', 'up')
print(r)
print()

for _ in range(3):
    r.x_rotate('bottom', 'left')

    print(r)
    print()

for _ in range(4):
    r.y_rotate('left', 'up')
    r.y_rotate('left', 'up')
    r.x_rotate('top', 'right')

for _ in range(5):
    r.y_rotate('left', 'up')
    r.x_rotate('top', 'right')
    r.y_rotate('right', 'down')
r.x_rotate('bottom', 'left')
print(r)
print()
r.z_rotate('front', 'clockwise')
print(r)
