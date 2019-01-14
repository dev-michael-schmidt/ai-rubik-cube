from rubiks_cube import RubiksCube

r = RubiksCube()
print(r)
print()

#r.vertical_rotate('right', 'up')
r.vertical_rotate('right', 'down')

r.horizontal_rotate('middle', 'left')

print(r)
