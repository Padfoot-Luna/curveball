import unittest

from utilities.networkx import create_networkx_graph, is_isomorphic, create_networkx_digraph


class MyTestCase(unittest.TestCase):
    def test_create_networkx_graph(self):
        """
        Checks creation of a networkx graph from an adjacency list
        """
        test_dataset = [
            {
                'adjacency_list': {},
                'expected_nodes': [],
                'expected_edges': []
            }, {
                'adjacency_list': {
                    1: {2, 3},
                    2: {1, 3},
                    3: {1, 2}
                },
                'expected_nodes': [1, 2, 3],
                'expected_edges': [(1, 2), (1, 3), (2, 3)]
            }, {
                'adjacency_list': {
                    1: {2, 3},
                    2: {3},
                    3: {}
                },
                'expected_nodes': [1, 2, 3],
                'expected_edges': [(1, 2), (1, 3), (2, 3)]
            }
        ]
        for test_data in test_dataset:
            with self.subTest(test_data=test_data):
                graph = create_networkx_graph(test_data['adjacency_list'])
                self.assertListEqual(graph.nodes(), test_data['expected_nodes'])
                self.assertCountEqual(graph.edges(), test_data['expected_edges'])

    def test_create_networkx_digraph(self):
        """
        Checks creation of a networkx digraph from an adjacency list
        """
        test_dataset = [
            {
                'adjacency_list': {},
                'expected_nodes': [],
                'expected_edges': []
            }, {
                'adjacency_list': {
                    1: {2, 3},
                    2: {1, 3},
                    3: {1, 2}
                },
                'expected_nodes': [1, 2, 3],
                'expected_edges': [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
            }, {
                'adjacency_list': {
                    1: {2, 3},
                    2: {3},
                    3: {}
                },
                'expected_nodes': [1, 2, 3],
                'expected_edges': [(1, 2), (1, 3), (2, 3)]
            }
        ]
        for test_data in test_dataset:
            with self.subTest(test_data=test_data):
                graph = create_networkx_digraph(test_data['adjacency_list'])
                self.assertListEqual(graph.nodes(), test_data['expected_nodes'])
                self.assertCountEqual(graph.edges(), test_data['expected_edges'])

    def test_is_isomorphic_graph(self):
        """
        Checks is_isomorphic function for undirected graphs
        """
        test_dataset = [
            {
                'g': create_networkx_graph({1: {2, 3}, 2: {1}, 3: {1}}),
                'graphs': [
                    create_networkx_graph({1: {2}, 2: {1, 3}, 3: {2}}),
                    create_networkx_graph({1: {3}, 2: {3}, 3: {1, 2}}),
                ],
                'is_isomorphic': True
            }, {
                'g': create_networkx_graph({1: {2, 3}, 2: {1}, 3: {1}}),
                'graphs': [
                    create_networkx_graph({1: {2}, 2: {1, 3}, 3: {2}}),
                    create_networkx_graph({1: {2}, 2: {3}, 3: {1}}),
                ],
                'is_isomorphic': True
            }, {
                'g': create_networkx_graph({1: {2, 3}, 2: {1}, 3: {1}}),
                'graphs': [
                    create_networkx_graph({1: {2}, 2: {1}, 3: {}}),
                    create_networkx_graph({1: {2}, 2: {3}, 3: {1}}),
                ],
                'is_isomorphic': False
            }
        ]
        for test_data in test_dataset:
            with self.subTest(test_data=test_data):
                isomorphic = is_isomorphic(g=test_data['g'], graphs=test_data['graphs'])
                self.assertEqual(isomorphic, test_data['is_isomorphic'])

    def test_is_isomorphic_digraph(self):
        """
        Checks is_isomorphic function for directed graphs
        """

        # these 3 graphs are isomorphic
        digraph1 = create_networkx_digraph({1: {2, 3}, 2: {}, 3: {}})
        digraph2 = create_networkx_digraph({1: {}, 2: {1, 3}, 3: {}})
        digraph3 = create_networkx_digraph({1: {}, 2: {}, 3: {1, 2}})

        test_dataset = [
            {
                'g': digraph1,
                'graphs': [
                    digraph1,
                    digraph2,
                    digraph3
                ],
                'is_isomorphic': True
            }, {
                'g': digraph1,
                'graphs': [
                    digraph2,
                    digraph3
                ],
                'is_isomorphic': True
            }, {
                'g': digraph1,
                'graphs': [
                    digraph3
                ],
                'is_isomorphic': True
            }, {
                'g': digraph1,
                'graphs': [
                    digraph2,
                ],
                'is_isomorphic': True
            }, {
                'g': digraph1,
                'graphs': [
                    digraph2,
                    create_networkx_digraph({1: {2}, 2: {3}, 3: {1}}),
                ],
                'is_isomorphic': True
            }, {
                'g': digraph1,
                'graphs': [
                    create_networkx_digraph({1: {2}, 2: {1}, 3: {}}),
                    create_networkx_digraph({1: {2}, 2: {3}, 3: {1}}),
                ],
                'is_isomorphic': False
            }
        ]
        for test_data in test_dataset:
            with self.subTest(test_data=test_data):
                isomorphic = is_isomorphic(g=test_data['g'], graphs=test_data['graphs'])
                self.assertEqual(isomorphic, test_data['is_isomorphic'])


if __name__ == '__main__':
    unittest.main()
