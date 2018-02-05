import unittest
from collections import defaultdict

import networkx as nx

from tests.datasets.directed.dataset import a_directed_graph
from utilities.networkx import create_networkx_digraph


class TestDatasets(unittest.TestCase):
    def test_a_directed_graph(self):
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
            (1, 0): 1,
            (0, 1): 1,
            (1, 1): 4,
            (1, 2): 1,
            (2, 1): 1,
        }
        for i, adjacency_list in enumerate(a_directed_graph):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                degree_distribution = defaultdict(int)
                for node, neighbours in adjacency_list.items():
                    out_degree = len(neighbours)
                    in_degree = sum([1 for x in adjacency_list.keys() if node in adjacency_list[x]])
                    degree_distribution[(in_degree, out_degree)] += 1
                self.assertDictEqual(degree_distribution, expected_degree_distribution)

    def test_number_of_graphs(self):
        self.assertEqual(len(a_directed_graph), 167)

    def test_no_self_loop(self):
        for i, adjacency_list in enumerate(a_directed_graph):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                for node, neighbors in adjacency_list.items():
                    self.assertTrue(node not in neighbors)

    def test_isomorphism(self):
        """
        Check whether our different graphs are isomorphisms (they shall not be)
        """
        for i in range(len(a_directed_graph)):
            graph_i = create_networkx_digraph(a_directed_graph[i])
            for j in range(i + 1, len(a_directed_graph)):
                with self.subTest(i=i, j=j, adj_list_i=a_directed_graph[i], adj_list_j=a_directed_graph[j]):
                    graph_j = create_networkx_digraph(a_directed_graph[j])
                    is_isomorphic = nx.is_isomorphic(graph_i, graph_j)
                    self.assertFalse(is_isomorphic)


if __name__ == '__main__':
    unittest.main()
