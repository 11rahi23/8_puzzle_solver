import numpy as np
import math

class board:
	zero=0
	cost=0

	def __init__(self, state, board_size, parent = None, operator = None, depth = 0):
		self.state=state
		#print("board state:", self.state)
		self.board_size=board_size
		#print ("Board size :",self.board_size)
		self.parent =parent
		self.operator=operator
		self.zero=self.find_0()
		self.depth=depth
		self.cost=self.depth+self.manhattah()
		self.array_size=self.board_size*self.board_size
		#print("array_size: ", self.array_size)

	def __lt__(self, other):
		if self.cost != other.cost:
			return self.cost < other.cost
		else:
			op_pr = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
			return op_pr[self.operator] < op_pr[other.operator]

	def array_size(self):
		return self.board_size*self.board_size

	def goal_test(self):
		goal_state=np.arange(9)
		if np.array_equal(self.state, goal_state):
			return True
		else:
			return False

	def find_0(self):
		for i in range(9):
			if self.state[i]==0:
				#print("i:",i)
				return i


	def manhattah(self):
		#index function is defined later
		state=self.index(self.state)
		goal=self.index(np.arange(9))
		board_size=self.board_size

		#print("manhattan :")
		#print((sum((abs(state//board_size-goal//board_size)+abs(state%board_size-goal%board_size))[1:])))

		return sum((abs(state//board_size-goal//board_size)+abs(state%board_size-goal%board_size))[1:])

	def index(self,state):
		index = np.array(range(9))
		for i, j in enumerate(state):
			index[j] = i

		#print(index)
		return index

	def swap(self, i, j):
		new_state = np.array(self.state)
		new_state[i], new_state[j] = new_state[j], new_state[i]
		return new_state

	def up(self):
		if self.zero>(self.board_size-1):
			return board(self.swap(self.zero, self.zero-self.board_size), self.board_size, self, 'Up', self.depth+1)
		else:
			return None

	def down(self):
		if self.zero<(self.board_size*(self.board_size-1)):
			return board(self.swap(self.zero, self.zero+self.board_size), self.board_size, self, 'Down', self.depth+1 )
		else:
			return None

	def left(self):
		if self.zero%self.board_size != 0:
			return board(self.swap(self.zero, self.zero-1), self.board_size, self, 'Left', self.depth+1 )
		else:
			return None


	def right(self):
		if (self.zero+1)%self.board_size != 0:
			return board(self.swap(self.zero, self.zero+1), self.board_size, self, 'Right', self.depth+1 )
		else:
			return None

	def neighbours(self):
		neighbours = [self.up(), self.down(), self.left(), self.right()]
		return list(filter(None, neighbours))










