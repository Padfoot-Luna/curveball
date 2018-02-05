import unittest
from collections import defaultdict

import networkx as nx

from tests.datasets.bipartite.dataset import a_small_bipartite_graph
from utilities.networkx import create_networkx_digraph


class TestDatasets(unittest.TestCase):
    def test_a_bipartite_graph(self):
        """
        Loads the example of an undirected graph with 8 nodes
        and the following degree distribution:
        1 nodes with in-degree k_in = 1 and out-degree k_out = 0
        1 nodes with in-degree k_in = 0 and out-degree k_out = 1
        4 nodes with in-degree k_in = 1 and out-degree k_out = 1
        1 nodes with in-degree k_in = 1 and out-degree k_out = 2
        1 nodes with in-degree k_in = 2 and out-degree k_out = 1

        CHecks the degree distributions for all adjacency_lists
        """
        expected_degree_distribution = {
            1: 2,
            2: 1,
        }
        for i, adjacency_list in enumerate(a_small_bipartite_graph):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                degree_distribution = defaultdict(int)
                for node, neighbours in adjacency_list.items():
                    degree = len(neighbours)
                    degree_distribution[degree] += 1
                self.assertDictEqual(degree_distribution, expected_degree_distribution)

    def test_number_of_graphs(self):
        self.assertEqual(len(a_small_bipartite_graph), 0)

    def test_no_self_loop(self):
        for i, adjacency_list in enumerate(a_small_bipartite_graph):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                for node, neighbors in adjacency_list.items():
                    self.assertTrue(node not in neighbors)

    def test_isomorphism(self):
        """
        Check whether our different graphs are isomorphisms (they shall not be)
        """
        self.fail('find out how to test isomorphism for bipartite graphs')


if __name__ == '__main__':
    unittest.main()
