import unittest
from collections import Counter

import networkx as nx

from tests.datasets.undirected.dataset import an_undirected_graph
from utilities.networkx import create_networkx_graph


class TestDatasets(unittest.TestCase):
    def test_an_undirected_graph(self):
        """
        Loads the example of an undirected graph with 8 nodes
        and the following degree distribution:
        2 nodes with degree k = 1
        4 nodes with degree k = 2
        2 nodes with degree k = 3

        CHecks the degree distributions for all adjacency_lists
        """
        expected_degree_distribution = {1: 2, 2: 4, 3: 2}
        for i, adjacency_list in enumerate(an_undirected_graph):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                c = Counter([len(v) for _, v in adjacency_list.items()])
                self.assertDictEqual(c, expected_degree_distribution)

    def test_number_of_graphs(self):
        self.assertEqual(len(an_undirected_graph), 27)

    def test_no_self_loop(self):
        for i, adjacency_list in enumerate(an_undirected_graph):
            with self.subTest(i=i, adjacency_list=adjacency_list):
                for node, neighbors in adjacency_list.items():
                    self.assertTrue(node not in neighbors)

    def test_isomorphism(self):
        """
        Check whether our different graphs are isomorphisms (they shall not be)
        """
        for i in range(len(an_undirected_graph)):
            graph_i = create_networkx_graph(an_undirected_graph[i])
            for j in range(i + 1, len(an_undirected_graph)):
                with self.subTest(i=i, j=j, adj_list_i=an_undirected_graph[i], adj_list_j=an_undirected_graph[j]):
                    graph_j = create_networkx_graph(an_undirected_graph[j])
                    is_isomorphic = nx.is_isomorphic(graph_i, graph_j)
                    self.assertFalse(is_isomorphic)


if __name__ == '__main__':
    unittest.main()
