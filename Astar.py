import heapq
import Board
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
		cost = []

		while self.frontier:
			#curr1=heapq.heappop(frontier)
			curr1=frontier.pop(0)
			#print("curr1:",curr1)
			print("iter: ", iterate)
			curr=Board.board(curr1, self.board_size)
			#print ("curr.state: ", curr.state)
			self.explored_nodes.append(curr.state)
			#print("explored_nodes: ", self.explored_nodes)

			#Goal test
			if curr.goal_test():
				print("goal test: true")
				self.set_solution(curr)
				break
			else:
				print("goal test: false")

			#custom neighbours() function assigns neighbour states for each state. Now iterating	
			for neighbour in curr.neighbours():
				print("neighbour_state:",neighbour.state)
				print("frontier: ", frontier)


				#for i in frontier:
				#	print("i: ", i)
				#	if neighbour.state in i:
				#		break
				
				frontier.append(neighbour.state)
				cost.append(neighbour.cost)
				print("neighbour_cost: ", neighbour.cost)

				#if neighbour.state not in frontier:
				#	frontier.append(neighbour.state)
				#	print("frontier now:", frontier)
			print("frontier: ",frontier)
			print("cost: ", cost)

			cost = sorted(cost)

			print("sorted cost: ", cost)

			#cost=dict(sorted(cost.items(), key=lambda item: item[1]))

			(k := next(iter(reach_cost)), reach_cost.pop(k))
			lcost_next = list(reach_cost.keys())[0]
			frontier.append(lcost_next)


				#print ("neighbour.state:",neighbour.state)
				#if not any(np.array_equal(x, neighbour.state) for x in self.explored_nodes):
					#if not any(np.array_equal(x, neighbour.state) for x in frontier):
						#heapq.heappush(frontier, tuple(neighbour.state))
						#print("frontier :", frontier)
						#self.max_depth=max(self.max_depth, neighbour.depth)
						#print("max_depth :", self.max_depth)
			



			iterate+=1





		

	def set_solution(self, curr):
		
		while curr.parent is not None:
			path.append(curr_state)
			curr=curr.parent

		path.append(init_state)

		print (path)
		return path





