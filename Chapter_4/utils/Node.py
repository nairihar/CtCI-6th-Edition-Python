class Node:
	def __init__(self, name):
		self.name = name
		self.adjacents = []

	def add_adjacent(self, node):
		self.adjacents.append(node)

	def get_adjacents(self):
		return self.adjacents
