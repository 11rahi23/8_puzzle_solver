from Board import board
import numpy as np

class Astar:

	solution =None
	path = []
	parent = []

	def __init__(self, initial_state, goal_state, board_size):
		self.init_state = initial_state
		self.goal_state = goal_state
		self.frontier = []
		self.explored_nodes = []
		self.board_size=board_size
		print ("Board size 1:", self.board_size)
		self.max_depth=0

	def solve(self):
		#Heap pushing initial state in frontier, to create a sorted stack
		frontier= self.frontier
		#heapq.heappush(frontier, tuple(self.init_state))
		frontier.append(self.init_state)

		print("Initial Frontier: ", frontier)

		iterate = 0
		parent = []
		path = []
		cost = {}

		while self.frontier:
			#curr1=heapq.heappop(frontier)
			curr1=frontier.pop(0)
			#print("curr1:",curr1)
			print("iter: ", iterate)
			curr=board(curr1, self.board_size)
			print("current state:", curr.state, " cost: ", curr.cost)
			#print ("curr.state: ", curr.state)
			self.explored_nodes.append(curr)
			#print("explored_nodes: ", self.explored_nodes)

			#Goal test
			if curr.goal_test():
				print("goal test: true")
				self.set_solution(curr)
				return 
			else:
				print("goal test: false")

			#custom neighbours() function assigns neighbour states for each state. Now iterating	
			for neighbour in curr.neighbours():
				#print("neighbour_state:",neighbour.state)
				print("frontier: ", frontier)
				print("neighbour ", neighbour.state, "cost: ", neighbour.cost)
				if curr.parent != neighbour:
					neighbour.parent=curr

				print("parent of ", neighbour.state, "is ", curr.state)
				if not contains(neighbour not in self.explored_nodes:
					self.explored_nodes.append(neighbour)



				#for i in frontier:
				#	print("i: ", i)
				#	if neighbour.state in i:
				#		break
				
				#frontier.append(neighbour.state)
				#self.explored_nodes.append(neighbour)
				#path.append(neighbour)


				#if neighbour.state not in frontier:
				#	frontier.append(neighbour.state)
				#	print("frontier now:", frontier)
			print("frontier: ",frontier)
			self.explored_nodes.sort(key=lambda x: x.cost)
			print("explored_nodes[0] :", self.explored_nodes[0].state)
			print("explored_nodes[1] :", self.explored_nodes[1].state)
			if np.array_equal(self.explored_nodes[0].state, curr.state):
				print("trigger")
				lcost_next=self.explored_nodes[1].state
			else:
				lcost_next=self.explored_nodes[0].state
			print("lcost_next: ", lcost_next)
			if lcost_next not in frontier:
				frontier.append(lcost_next)

			#print("explored nodes: ", self.explored_nodes)
			
			print("frontier at the end of iteration ", iterate, "is :", frontier)



			iterate+=1





		

	def set_solution(self, curr):

		path = []
		
		while curr.parent is not None:
			print("curr state to append in path: ", curr.state)
			path.append(curr.state)
			curr=curr.parent

		path.append(self.init_state)

		print ("path to goal is: ", path)
		return path
