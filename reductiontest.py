import unittest
import networkx as nx
import reduction_steps_graph_gen as functions


class TestUnderconstrained(unittest.TestCase):

	def test_underconstrained_3K_1(self):
		# Three underconstrained nodes: 1, 2, 3
		G = nx.Graph()
		G.add_nodes_from(range(4))
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(1,2)
		functions.undercon(G, 3)

		F = nx.Graph()
		F.add_nodes_from(range(1))

		self.assertEqual(F.edges(), G.edges())

	def test_underconstrained_3K_2(self):
		# Two underconstrained nodes: 2, 3
		G = nx.Graph()
		G.add_nodes_from(range(4))
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(1,2)
		G.add_edge(1,3)
		functions.undercon(G, 3)

		F = nx.Graph()
		F.add_nodes_from(range(2))
		F.add_edge(0,1)

		self.assertEqual(F.edges(), G.edges())

	def test_underconstrained_3K_3(self):
		# Three underconstrained nodes: 5, 7, 8
		G = nx.Graph()
		G.add_nodes_from(range(8))
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(1,2)
		G.add_edge(1,4)
		G.add_edge(2,4)
		G.add_edge(3,5)
		G.add_edge(3,6)
		G.add_edge(4,5)
		G.add_edge(6,7)
		G.add_edge(6,8)
		functions.undercon(G, 3)

		F = nx.Graph()
		F.add_edge(0,1)
		F.add_edge(0,2)
		F.add_edge(0,3)
		F.add_edge(1,2)
		F.add_edge(1,4)
		F.add_edge(2,4)
		F.add_edge(3,6)

		self.assertEqual(F.edges(), G.edges())


	def test_underconstrained_4K_1(self):
		# Two underconstrained nodes: 1, 3
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(0,4)
		G.add_edge(1,2)
		G.add_edge(1,4)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(3,4)
		functions.undercon(G, 4)

		F = nx.Graph()
		F.add_edge(0,2)
		F.add_edge(0,4)
		F.add_edge(2,4)

		self.assertEqual(F.edges(), G.edges())

	def test_underconstrained_4K_2(self):
		# Two underconstrained nodes: 1, 4
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(0,4)
		G.add_edge(0,5)
		G.add_edge(0,6)
		G.add_edge(1,2)
		G.add_edge(2,3)
		G.add_edge(2,5)
		G.add_edge(2,6)
		G.add_edge(3,4)
		G.add_edge(3,5)
		G.add_edge(3,6)
		G.add_edge(5,6)
		functions.undercon(G, 4)

		F = nx.Graph()
		F.add_edge(0,2)
		F.add_edge(0,3)
		F.add_edge(0,5)
		F.add_edge(0,6)
		F.add_edge(2,3)
		F.add_edge(2,5)
		F.add_edge(2,6)
		F.add_edge(3,5)
		F.add_edge(3,6)
		F.add_edge(5,6)

		self.assertEqual(F.edges(), G.edges())

	def test_underconstrained_4K_3(self):
		# No underconstrained nodes
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(0,4)
		G.add_edge(1,2)
		G.add_edge(1,3)
		G.add_edge(1,4)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(3,4)
		functions.undercon(G, 4)

		F = nx.Graph()
		F.add_edge(0,1)
		F.add_edge(0,2)
		F.add_edge(0,3)
		F.add_edge(0,4)
		F.add_edge(1,2)
		F.add_edge(1,3)
		F.add_edge(1,4)
		F.add_edge(2,3)
		F.add_edge(2,4)
		F.add_edge(3,4)

		self.assertEqual(F.edges(), G.edges())

class TestSubsumed(unittest.TestCase):

	def test_subsumed_3K_1(self):
		# One subsumed node: 6. Checks if the function removes the right node.
		G = nx.Graph()
		G.add_edge(0,2)
		G.add_edge(1,2)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(2,5)
		G.add_edge(6,3)
		G.add_edge(6,4)
		G.add_edge(6,5)
		functions.subsumed(G, 3)

		F = nx.Graph()
		F.add_edge(0,2)
		F.add_edge(1,2)
		F.add_edge(2,3)
		F.add_edge(2,4)
		F.add_edge(2,5)

		self.assertEqual(F.edges(), G.edges())

	def test_subsumed_3K_2(self):
		# One subsumed node: 4. Checks if the function works if 
		# the nodes in between are connected to each-other.
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(1,2)
		G.add_edge(1,3)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(3,4)
		G.add_edge(1,5)
		G.add_edge(5,4)
		functions.subsumed(G, 3)

		F = nx.Graph()
		F.add_edge(0,1)
		F.add_edge(1,2)
		F.add_edge(1,3)
		F.add_edge(2,3)
		F.add_edge(1,5)

		self.assertEqual(F.edges(), G.edges())

	def test_subsumed_3K_3(self):
		# No subsumed nodes for a 3K graph. Checks if the function
		# doesn't remove too much.
		G = nx.Graph()
		G.add_edge(0,2)
		G.add_edge(1,2)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(2,5)
		G.add_edge(6,3)
		G.add_edge(6,4)
		G.add_edge(6,5)
		G.add_edge(6,7)
		functions.subsumed(G, 3)

		F = nx.Graph()
		F.add_edge(0,2)
		F.add_edge(1,2)
		F.add_edge(2,3)
		F.add_edge(2,4)
		F.add_edge(2,5)
		F.add_edge(6,3)
		F.add_edge(6,4)
		F.add_edge(6,5)
		F.add_edge(6,7)

		self.assertEqual(F.edges(), G.edges())

	def test_subsumed_3K_4(self):
		# Two subsumed nodes: 0, 8. Checks if the function works if 
		# there are multiple subsumed nodes in a graph.
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(4,1)
		G.add_edge(4,2)
		G.add_edge(4,3)
		G.add_edge(4,9)
		G.add_edge(4,10)
		G.add_edge(3,5)
		G.add_edge(3,6)
		G.add_edge(3,7)
		G.add_edge(8,5)
		G.add_edge(8,6)
		G.add_edge(8,7)
		functions.subsumed(G, 3)

		F = nx.Graph()
		F.add_edge(4,1)
		F.add_edge(4,2)
		F.add_edge(4,3)
		F.add_edge(4,9)
		F.add_edge(4,10)
		F.add_edge(3,5)
		F.add_edge(3,6)
		F.add_edge(3,7)

		self.assertEqual(F.edges(), G.edges())

	def test_subsumed_4K_1(self):
		# One subsumed node: 0. Checks if the function works
		# with a different value for K.
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,3)
		G.add_edge(0,4)
		G.add_edge(1,2)
		G.add_edge(3,4)
		G.add_edge(5,1)
		G.add_edge(5,2)
		G.add_edge(5,3)
		G.add_edge(5,4)
		G.add_edge(5,6)
		functions.subsumed(G, 4)

		F = nx.Graph()
		F.add_edge(1,2)
		F.add_edge(3,4)
		F.add_edge(5,1)
		F.add_edge(5,2)
		F.add_edge(5,3)
		F.add_edge(5,4)
		F.add_edge(5,6)
		self.assertEqual(F.edges(), G.edges())

	def test_subsumed_4K_2(self):
		# Subsumed node for 3K but not for 4K. Checks if 
		# the function doesn't remove too much.
		G = nx.Graph()
		G.add_edge(0,2)
		G.add_edge(1,2)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(2,5)
		G.add_edge(6,3)
		G.add_edge(6,4)
		G.add_edge(6,5)
		functions.subsumed(G, 4)

		F = nx.Graph()
		F.add_edge(0,2)
		F.add_edge(1,2)
		F.add_edge(2,3)
		F.add_edge(2,4)
		F.add_edge(2,5)
		F.add_edge(6,3)
		F.add_edge(6,4)
		F.add_edge(6,5)

		self.assertEqual(F.edges(), G.edges())

class TestSymmetry(unittest.TestCase):

	def test_symmetry_3K_1(self):
		# Mergable nodes: 0, 3. Checks if the function can
		# detect two symmetrical nodes and merge them.
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,7)
		G.add_edge(0,8)
		G.add_edge(1,2)
		G.add_edge(1,3)
		G.add_edge(2,3)
		G.add_edge(3,4)
		G.add_edge(3,5)
		G.add_edge(3,6)

		G = functions.symmetry(G, 3)

		F = nx.Graph()
		F.add_edge(0,7)
		F.add_edge(0,8)
		F.add_edge(1,2)
		F.add_edge(1,0)
		F.add_edge(2,0)
		F.add_edge(0,4)
		F.add_edge(0,5)
		F.add_edge(0,6)

		self.assertEqual(F.edges(), G.edges())

	def test_symmetry_3K_2(self):
		# Mergable nodes: 0, 3, 6. Checks if the function can
		# detect multiple symmetrical nodes and merge them into one.
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(0,2)
		G.add_edge(0,9)
		G.add_edge(1,2)
		G.add_edge(1,3)
		G.add_edge(2,3)
		G.add_edge(3,4)
		G.add_edge(3,5)
		G.add_edge(4,5)
		G.add_edge(4,6)
		G.add_edge(5,6)
		G.add_edge(6,7)
		G.add_edge(6,8)

		G = functions.symmetry(G, 3)

		F = nx.Graph()
		F.add_edge(0,1)
		F.add_edge(0,2)
		F.add_edge(0,9)
		F.add_edge(1,2)
		F.add_edge(0,4)
		F.add_edge(0,5)
		F.add_edge(4,5)
		F.add_edge(0,7)
		F.add_edge(0,8)

		self.assertEqual(F.edges(), G.edges())

	def test_symmetry_4K_1(self):
		# Mergable nodes: 2-6 and 11-5. Checks if the function can
		# detect multiple different symmetrical nodes and merge them.
		G = nx.Graph()
		G.add_edge(0,2)
		G.add_edge(1,2)
		G.add_edge(2,3)
		G.add_edge(2,4)
		G.add_edge(2,5)
		G.add_edge(3,4)
		G.add_edge(3,5)
		G.add_edge(4,5)
		G.add_edge(6,3)
		G.add_edge(6,4)
		G.add_edge(6,5)
		G.add_edge(6,7)
		G.add_edge(5,8)
		G.add_edge(5,9)
		G.add_edge(5,10)
		G.add_edge(8,9)
		G.add_edge(8,10)
		G.add_edge(9,10)
		G.add_edge(11,8)
		G.add_edge(11,9)
		G.add_edge(11,10)
		G.add_edge(11,12)
		G = functions.symmetry(G, 4)

		F = nx.Graph()
		F.add_edge(0,2)
		F.add_edge(1,2)
		F.add_edge(2,3)
		F.add_edge(2,4)
		F.add_edge(2,5)
		F.add_edge(3,4)
		F.add_edge(3,5)
		F.add_edge(4,5)
		F.add_edge(2,7)
		F.add_edge(5,8)
		F.add_edge(5,9)
		F.add_edge(5,10)
		F.add_edge(8,9)
		F.add_edge(8,10)
		F.add_edge(9,10)
		F.add_edge(5,10)
		F.add_edge(5,12)

		self.assertEqual(F.edges(), G.edges())

	def test_symmetry_4K_2(self):
		# This is a merable graph for 3K but not for 4K.
		# Checks whether the function doesn't remove too much.
		G = nx.Graph()
		G.add_edge(0,1)
		G.add_edge(1,2)
		G.add_edge(0,4)
		G.add_edge(1,2)
		G.add_edge(1,3)
		G.add_edge(2,3)
		G.add_edge(3,5)

		G = functions.symmetry(G, 3)

		F = nx.Graph()
		F.add_edge(0,1)
		F.add_edge(1,2)
		F.add_edge(0,4)
		F.add_edge(1,2)
		F.add_edge(1,3)
		F.add_edge(2,3)
		F.add_edge(3,5)

		self.assertEqual(F.edges(), G.edges())



if __name__ == '__main__':
    unittest.main()