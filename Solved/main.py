import sys
import numpy as np
from board import Board
from astar import Astar


def main():

	p=np.array(eval(sys.argv[2]))
	print("p: ", p)
	init=Board(p)
	alg=sys.argv[1]

	if alg == 'Astar':
		s=Astar(p)

	s.solve()

if __name__=="__main__":
	main()



