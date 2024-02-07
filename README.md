# Leonardo

A python library for working with the metallic means.

## Examples

### Working with Constants

```python

from leonardo import *


str(Gold.ratio)
# 1.618

str(Silver.ratio)
# 2.414

str(Bronce.ratio)
# 3.303

str(Gold.angle)
# '137.51°'

str(Silver.angle)
# '105.44°'

str(Bronce.angle)
# '83.67°'

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

A golden angle is an object with common units as properties.

```python

from leonardo import Gold

Gold.angle
# Angle(fraction=0.38196601125010515)

[a.radians for a in Gold.angle_sequence[:5]]
# [2.399963229728653, 4.799926459457306, 7.199889689185959, 9.599852918914612]

[a.radians_canonic for a in Gold.angle_sequence[:5]]
# [2.399963229728653, 4.799926459457306, 0.9167043820063725, 3.316667611735026]

[a.degrees for a in Gold.angle_sequence[:5]]
# [137.50776405003785, 275.0155281000757, 412.5232921501135, 550.0310562001514]

[a.degrees_canonic for a in Gold.angle_sequence[:5]]
# [137.50776405003785, 275.0155281000757, 52.52329215011349, 190.0310562001514]

[a.fraction for a in Gold.angle_sequence[:5]]
# [0.3819660112501051,
# 0.7639320225002102,
# 1.1458980337503153,
# 1.5278640450004204]

[a.fraction_canonic for a in Gold.angle_sequence[:5]]
# [0.3819660112501051,
# 0.7639320225002102,
# 0.1458980337503153,
# 0.5278640450004204]

Gold.angle.complex
# (-0.7373688780783197+0.6754902942615238j)

x = Gold.angle.complex.real
x
# -0.7373688780783197

y = Gold.angle.complex.imag
y
# 0.6754902942615238

for angle in Gold.angle_sequence[:5]:
    p = angle.complex.real, angle.complex.imag
    print(p)
# (-0.7373688780783197, 0.6754902942615238)
# (0.08742572471695988, -0.9961710408648278)
# (0.6084388609788626, 0.7936007512916959)
# (-0.9847134853154287, -0.17418195037931164)

```

This is still an early version and no interfaces are guaranteed to stay stable.

## Running Tests

Run the test-suite to see if the code base is behaving as expected.

```bash
python3 -m unittest
```
