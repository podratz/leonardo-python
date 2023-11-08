# Leonardo

A python library for working with the metallic means.

## Examples

``` python

from leonardo import BronceSequence, SilverSequence, GoldenSequence

# Construct the metallic sequences.
bronce = BronceSequence()
silver = SilverSequence()
gold   = GoldenSequence()

# Get the metallic ratios.
bronce()               # 3.302775637731995
silver()               # 2.414213562373095
gold()                 # 1.618033988749895 

# Get 5 consecutive elements from a metallic sequence.
gold[0:5]              # [1.0,
                       #  1.618033988749895,
                       #  2.618033988749895,
                       #  4.23606797749979,
                       #  6.854101966249686]

# Given one size, compute aesthetically pleasing scalings.
# E.g. font-sizes, proportions of buttons, ...
gold = GoldenSequence(17)
gold[-2:3]             # [6.4934221912517875,
                       #  10.506577808748212,
                       #  17.0,
                       #  27.50657780874821,
                       #  44.50657780874821]

# To keep your namespace tidy, import with an alias.
import leonardo as ld
gold = ld.GoldenSequence()
gold(4)                # 6.854101966249686

# If all you need is the metallic ratio itself, you can access
# it directly without the overhead of an object construction.
ld.bronce_ratio        # 3.302775637731995
ld.silver_ratio        # 2.414213562373095
ld.golden_ratio        # 1.618033988749895

```
