# Leonardo

A python library for working with the metallic means.

## Examples

``` python

from leonardo import golden_sequence as gold
from leonardo import silver_sequence as silver
from leonardo import bronce_sequence as bronce

# Get the metallic means.
gold()                 # 1.618033988749895 
silver()               # 2.414213562373095
bronce()               # 3.302775637731995

# Given one size, compute aesthetically pleasing scalings.
# E.g. font-sizes, proportions of buttons, ...
gold(-1, 17)           # 10.506577808748212
gold(1, 17)            # 27.50657780874821
gold(2, 17)            # 44.50657780874821
gold(3, 17)            # 72.01315561749642

# To keep your namespace tidy, import with an alias.
import leonardo as ld
ld.golden_sequence(4)  # 6.854101966249686

# If all you need is the golden ratio itself, you can access
# it directly without the overhead of a function call.
ld.golden_ratio        # 1.618033988749895
ld.silver_ratio        # 2.414213562373095
ld.bronce_ratio        # 3.302775637731995

```
