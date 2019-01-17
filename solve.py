from rubik_cube import RubikCube

r = RubikCube()


r.y_rotate('left', 'down')
r.y_rotate('right', 'up')
print(r)
print()

for _ in range(3):
    r.x_rotate('bottom', 'left')

    print(r)
    print()

for _ in range(7):
    r.y_rotate('left', 'up')
    r.z_rotate('front', 'clockwise')
    r.y_rotate('left', 'up')
    r.x_rotate('top', 'right')
    r.x_rotate('top', 'right')
    r.z_rotate('back', 'clockwise')

for _ in range(32):
    r.z_rotate('front', 'anti-clockwise')
    r.y_rotate('left', 'up')
    r.x_rotate('top', 'right')
    r.z_rotate('front', 'clockwise')
    r.y_rotate('right', 'down')
    r.z_rotate('back', 'anti-clockwise')
r.x_rotate('bottom', 'left')
print(r)
print()
r.z_rotate('back', 'clockwise')
print(r)
