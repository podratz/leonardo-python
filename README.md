# Leonardo

A python library for working with the metallic means.

## Examples

### Working with Constants

```python

from leonardo import *


Gold.ratio
# 1.618033988749895

Silver.ratio
# 2.414213562373095

Bronce.ratio
# 3.302775637731995

Gold.angle(degrees=True)
# 137.50776405003788

Gold.angle() # defaults to radians
# 2.3999632297286535

```

### Working with Geometric Sequences
``` python

from leonardo import Gold


g = Gold() # g is a golden number

g17 = Gold(17) # g17 is a scaled golden number

g[-2:3] # prints the neighborhood of g
# [0.38196601125010515,
#  0.6180339887498948,
#  1.0,
#  1.618033988749895,
#  2.618033988749895]

# setting up fontsizes as a graphic designer
[body, subheadline, headline] = g17[-1:2]
body 
# 10.506577808748212
subheadline
# 17.0
headline
# 27.50657780874821

```

Make sure to read up on the silver and bronce ratio also, they are super cool.

### Working with Sequences of Angles

```python

from leonardo import Gold


angles = Gold.angle_sequence() # defaults to radians with no revolutions

angles[6]
# 1.8334087640127485

[angles[i] for i in range(4)]
# [0.0, 2.3999632297286535, 4.799926459457307, 7.1998896891859605]

angles = Gold.angle_sequence(revolves=True)

angles[6]
# 14.399779378371921

```

This is still an early version and no interfaces are guaranteed to stay stable.
