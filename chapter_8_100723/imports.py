import sandwiches
sandwiches.make_sandwich('Mayo', 'Cheese', 'Ham')
from sandwiches import make_sandwich
make_sandwich('Mayo', 'Cheese', 'Ham')
from sandwiches import make_sandwich as ms
ms('Mayo', 'Cheese', 'Ham')
import sandwiches as sw
sw.make_sandwich('Mayo', 'Cheese', 'Ham')
from sandwiches import *
make_sandwich('Mayo', 'Cheese', 'Ham')