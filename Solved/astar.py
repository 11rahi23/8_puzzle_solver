import numpy as np 
import board


class Astar():
	parent=None
	operator=None
	depth=0
	max_depth=0


	def __init__(self, initial_state):
		self.init_state=initial_state
		print("initial_state Astar: ", self.init_state)


	def predecessor(self, node):
		current=node
		print(current.state)
		predecessor = []
		predecessor.append(current.state)
		while current.parent is not None:
			print(current.parent.state)
			predecessor.append(current.parent.state)
			current=current.parent
		print("predecessor: ", predecessor)
		return predecessor

	def solve(self):
		self.frontier=[]
		self.frontier_nodes = []
		self.explored_nodes=[]
		self.explored_states = []
		self.iteration_ran = []
		self.uniterated = []

		self.frontier.append(self.init_state)

		iteration=0
		curr=board.Board(self.init_state)
		self.frontier_nodes.append(curr)

		while self.frontier_nodes:

			print("iteration: ", iteration)
			#curr1=self.frontier.pop(0)
			curr=self.frontier_nodes.pop(0)
			if not any(np.array_equal(curr.state, x) for x in self.iteration_ran):
				self.iteration_ran.append(curr)
			print("current state at iteration ", iteration, "is :",curr.state)
			if not any(np.array_equal(curr.state, x.state) for x in self.explored_nodes):
				self.explored_nodes.append(curr)
				self.explored_states.append(curr.state)


			if np.array_equal(curr.state, np.arange(9)):
				print("Goal test true")

				self.predecessor(self.explored_nodes[0])
				print ("done")
				return

			for neighbour in curr.neighbours():
				if not any(np.array_equal(neighbour.state, x.state) for x in self.explored_nodes):
					self.explored_nodes.append(neighbour)
					self.explored_states.append(neighbour.state)
					self.max_depth=max(self.max_depth, neighbour.depth)

			self.explored_nodes.sort(key=lambda x:x.cost)
			self.iteration_ran.sort(key=lambda x:x.cost)
			print("after sorting: ")
			for i in range(len(self.explored_nodes)):
				print(self.explored_nodes[i].state, "cost :", self.explored_nodes[i].cost )
			#lcost_next=self.explored_nodes[0].state
			#lcost_node_next=self.explored_nodes[0]
			#print("lcost_next :", lcost_next, "with cost: ", self.explored_nodes[0].cost)
			#second_lcost_next=self.explored_nodes[1].state
			#print("second_lcost_next :", second_lcost_next, "with cost: ", self.explored_nodes[1].cost)
			print("curr.state: ", curr.state, "with cost: ", curr.cost)

			#self.frontier.append(lcost_next)
			print("iteration_ran: ")
			for i in range(len(self.iteration_ran)):
				print(self.iteration_ran[i].state, "cost :", self.iteration_ran[i].cost )

			#for i in self.explored_nodes:
			#	if not all(np.array_equal(i.state, x.state) for x in self.iteration_ran):
			#		self.frontier_nodes.append(i)

			self.uniterated=set(self.explored_nodes)-set(self.iteration_ran)
			self.uniterated=list(self.uniterated)
			self.uniterated.sort(key=lambda x:x.cost)

			print("uniterated :")	
			for i in self.uniterated:
				print(i.state, "with cost: ", i.cost)
				if not any(np.array_equal(i, x) for x in self.frontier_nodes):
					self.frontier_nodes.append(i)
			self.frontier_nodes.sort(key=lambda x:x.cost)




			







			#if np.array_equal(lcost_next, curr.state):
			#	self.frontier.append(second_lcost_next)
			#	self.frontier_nodes.append(self.explored_nodes[1])
			#else: 
			#	self.frontier.append(lcost_next)
			#	self.frontier_nodes.append(self.explored_nodes[0])
			iteration+=1




