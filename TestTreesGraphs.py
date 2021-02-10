import unittest
from DataStructures.TreesGraphs import *

class TestTreesGraphs(unittest.TestCase):

    def testRouteExistence(self):
        small_graph = DirectedGraph()
        node_1 = DirectedGraphNode(1)
        node_2 = DirectedGraphNode(2)
        small_graph.add_node(node_1)
        small_graph.add_node(node_2)
        self.assertFalse(does_route_exists(small_graph, node_1, node_2))

        node_1.children.append(node_2)
        self.assertTrue(does_route_exists(small_graph, node_1, node_2))
        self.assertFalse(does_route_exists(small_graph, node_2, node_1))

    def testSomething(self):
        tree = construct_balanced_tree(range(10))
        self.assertEqual(len(list_of_nodes_per_level(tree)), 4)

        tree = construct_balanced_tree(range(20))
        self.assertEqual(len(list_of_nodes_per_level(tree)), 5)

        tree = construct_balanced_tree(range(100))
        self.assertEqual(len(list_of_nodes_per_level(tree)), 7)

if __name__ == '__main__':
    unittest.main()
