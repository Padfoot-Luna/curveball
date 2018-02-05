import unittest
from collections import defaultdict

import networkx as nx

from tests.datasets.classical.dataset import a_digraph_with_loops
from utilities.networkx import create_networkx_graph


class TestDatasets(unittest.TestCase):
    def test_an_undirected_graph(self):
        """
        Loads the example of an directed graph with 4 nodes
        and the following degree distribution:
        4 nodes with out-degree k_out = 1 and in-degree k_in = 1

        Checks the degree distributions for all adjacency_lists
        """
        expected_degree_distribution = {
            (1, 1): 4,
        }
        for i, adjacency_list in enumerate(a_digraph_with_loops):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                degree_distribution = defaultdict(int)
                for node, neighbours in adjacency_list.items():
                    out_degree = len(neighbours)
                    in_degree = sum([1 for x in adjacency_list.keys() if node in adjacency_list[x]])
                    degree_distribution[(in_degree, out_degree)] += 1
                self.assertDictEqual(degree_distribution, expected_degree_distribution)

    def test_number_of_graphs(self):
        self.assertEqual(len(a_digraph_with_loops), 5)

    def test_isomorphism(self):
        """
        Check whether our different graphs are isomorphisms (they shall not be)
        """
        for i in range(len(a_digraph_with_loops)):
            graph_i = create_networkx_graph(a_digraph_with_loops[i])
            for j in range(i + 1, len(a_digraph_with_loops)):
                with self.subTest(i=i,
                                  j=j,
                                  adj_list_i=a_digraph_with_loops[i],
                                  adj_list_j=a_digraph_with_loops[j]):
                    graph_j = create_networkx_graph(a_digraph_with_loops[j])
                    is_isomorphic = nx.is_isomorphic(graph_i, graph_j)
                    self.assertFalse(is_isomorphic)


if __name__ == '__main__':
    unittest.main()
