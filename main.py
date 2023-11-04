import sys

import numpy as np
import math
from Astar_new import Astar

init_state=np.array(eval(sys.argv[1]))
goal_state=np.arange(9)

print(init_state)
print(len(init_state))
board_size= int(math.sqrt(len(init_state)))
print(board_size)

s=Astar(init_state, goal_state, board_size)
s.solve()

