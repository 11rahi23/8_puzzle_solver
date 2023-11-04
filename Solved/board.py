import numpy as np 

class Board:
	def __init__(self, state, parent=None, operator=None, depth=0):
		self.state=np.array(state)
		print("self.state :", self.state)
		self.parent=parent
		self.operator=operator
		self.zero=self.find_zero()
		self.depth=depth
		self.cost=self.depth+self.manhattan()
		print("self.cost :", self.cost)

	def neighbours(self):
		neighbours=[self.up(), self.down(), self.left(), self.right()]
		return list(filter(None, neighbours))

	def goal_test(self):
		if np.array_equal(self.state, np.arange(9)):
			return True
		else:
			return False

	def find_zero(self):
		for i in np.arange(9):
			if self.state[i]==0:
				return i

	def index(self, state):
		index=np.array(range(9))
		for x,y in enumerate(state):
			index[y]=x

		return index


	def manhattan(self):
		state=self.index(self.state)
		goal=self.index(np.arange(9))

		manhattan=sum((abs(state//3-goal//3)+abs(state%3-goal%3))[1:])
		return manhattan

	def swap(self, i,j):
		new_state= np.array(self.state)
		new_state[i], new_state[j] = new_state[j], new_state[i]
		return new_state

	def up(self):
		if self.zero>2:
			return Board(self.swap(self.zero, self.zero-3), self, 'Up', self.depth+1)
		else:
			return None

	def down(self):
		if self.zero<6:
			return Board(self.swap(self.zero, self.zero+3), self, 'Down', self.depth+1)
		else:
			return None

	def left(self):
		if (self.zero)%3 != 0:
			return Board(self.swap(self.zero, self.zero-1), self, 'Left', self.depth+1)
		else: 
			return None

	def right(self):
		if (self.zero+1)%3 != 0:
			return Board(self.swap(self.zero, self.zero+1), self, 'Right', self.depth+1)
		else:
			return None

	def neighbours(self):
		neighbours = [self.up(), self.down(), self.left(), self.right()]
		return list(filter(None, neighbours))