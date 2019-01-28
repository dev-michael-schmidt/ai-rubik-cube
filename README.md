# ai-rubik-cube
Sovle a rubik's cube using the A* algorithm.

### Requirements
You can create a virtualenv and use `pip install -r requirements.txt`, but at the moment the only dependency is numpy.

## `class RubikCube` methods

The internal representation of the rubik cube is a `numpy.ndarray()` with a `(9, 12)` shape.

- `RubikCube.__init__(self)` Create a new instance of a RubikCube()
- `RubikCube.__str__(self)` Return a string of the internal representation.

```
>>> rc = RubikCube()
>>> print(rc)
      W W W
      W W W
      W W W
G G G R R R B B B O O O
G G G R R R B B B O O O
G G G R R R B B B O O O
      Y Y Y
      Y Y Y
      Y Y Y
>>>
```
- `RubikCube.scramble(self, moves=5000)` Scramble the rubik cube.
- `RubikCube.x_rotate(self, slot, direction)` perform a single rotation on the x axis.

```
>>> rc.x_rotate('top', 'left')
>>> rc.x_rotate('bottom', 'right')
>>> print(rc)
      W W W
      W W W
      W W W
Y Y Y G G G O O O B B B
B B B Y Y Y G G G O O O
O O O B B B Y Y Y G G G
      R R R
      R R R
      R R R
>>>

```
- `RubikCube.y_rotate(self, slot, direction)` perform a single rotation on the y axis.

```
>>> rc.y_rotate('left', 'up')
>>> rc.y_rotate('right', 'down')
>>> print(rc)
      Y W O
      Y W O
      Y W O
B B B R Y W G G G R O W
B B B R Y W G G G R O W
B B B R Y W G G G R O W
      O R Y
      O R Y
      O R Y
>>>
```

- `RubikCube.z_rotate(self, slot, direction)` perform a single rotation on the z axis.

```
>>> rc.z_rotate('front', 'clockwise')
>>> rc.z_rotate('back', 'anti-clockwise')
>>> print(rc)
      B B B
      W W W
      G G G
W G Y R R R W B Y O O O
W G Y R R R W B Y O O O
W G Y R R R W B Y O O O
      B B B
      Y Y Y
      G G G
>>>
```
