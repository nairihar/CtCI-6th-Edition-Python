class Graph:
	def __init__(self, name):
		self.name = name
		self.nodes = []

	def add_node(self, node):
		self.nodes.append(node)

	def get_node(self):
		return self.nodes

	def get_matrix(self):
