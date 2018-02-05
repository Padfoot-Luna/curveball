import unittest

from metrics.cooccurrence import cooccurrence_set_operation, compute_cooccurrence_graph, cooccurrence_bipartite


class MyTestCase(unittest.TestCase):
    def test_cooccurrence_set_operation(self):
        adjacency_list = {
            1: {2, 3, 4, 5},
            2: {1, 6},
            3: {1, 6},
            4: {1, 6},
            5: {1, 6},
            6: {2, 3, 4, 5}
        }

        self.assertEqual(cooccurrence_set_operation(1, 2, adjacency_list), 0)
        self.assertEqual(cooccurrence_set_operation(1, 3, adjacency_list), 0)
        self.assertEqual(cooccurrence_set_operation(1, 4, adjacency_list), 0)
        self.assertEqual(cooccurrence_set_operation(1, 5, adjacency_list), 0)
        self.assertEqual(cooccurrence_set_operation(1, 6, adjacency_list), 4)

        self.assertEqual(cooccurrence_set_operation(2, 3, adjacency_list), 2)
        self.assertEqual(cooccurrence_set_operation(2, 4, adjacency_list), 2)
        self.assertEqual(cooccurrence_set_operation(2, 5, adjacency_list), 2)
        self.assertEqual(cooccurrence_set_operation(2, 6, adjacency_list), 0)

        self.assertEqual(cooccurrence_set_operation(3, 4, adjacency_list), 2)
        self.assertEqual(cooccurrence_set_operation(3, 5, adjacency_list), 2)
        self.assertEqual(cooccurrence_set_operation(3, 6, adjacency_list), 0)

        self.assertEqual(cooccurrence_set_operation(4, 5, adjacency_list), 2)
        self.assertEqual(cooccurrence_set_operation(4, 6, adjacency_list), 0)

        self.assertEqual(cooccurrence_set_operation(5, 6, adjacency_list), 0)

    def test_compute_cooccurrence_graph(self):
        adjacency_list = {
            1: {2, 3, 4, 5},
            2: {1, 6},
            3: {1, 6},
            4: {1, 6},
            5: {1, 6},
            6: {2, 3, 4, 5}
        }

        expected_coocurrence_list = {
            1: {2: 0, 3: 0, 4: 0, 5: 0, 6: 4},
            2: {3: 2, 4: 2, 5: 2, 6: 0},
            3: {4: 2, 5: 2, 6: 0},
            4: {5: 2, 6: 0},
            5: {6: 0}
        }

        self.assertDictEqual(compute_cooccurrence_graph(adjacency_list), expected_coocurrence_list)

    def test_cooccurence_bipartite(self):
        adjacency_list = {
            1: {10, 11},
            2: {10, 11, 12},
            3: {11},
        }

        expected_coocc = {
            10: {11: 2, 12: 1},
            11: {12: 1},
        }

        actual_coocc = cooccurrence_bipartite(adjacency_list)

        self.assertEqual(len(actual_coocc), len(expected_coocc))
        self.assertDictEqual(expected_coocc[10], dict(actual_coocc[10]))
        self.assertDictEqual(expected_coocc[11], dict(actual_coocc[11]))


if __name__ == '__main__':
    unittest.main()
