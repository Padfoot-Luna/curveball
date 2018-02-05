import unittest

from metrics.memory.memory_usage import size_adjacency_matrix, size_adjacency_list, size_adjacency_map


class TestMemoryUsage(unittest.TestCase):
    def test_size_adjacency_matrix(self):
        self.assertEqual(size_adjacency_matrix(nb_nodes=20), 400)
        self.assertEqual(size_adjacency_matrix(nb_nodes=0), 0)
        self.assertEqual(size_adjacency_matrix(nb_nodes=10, element_size=3), 300)
        self.assertEqual(size_adjacency_matrix(nb_nodes=50, element_size=32), 80000)

    def test_size_adjacency_list(self):
        degree_distribution = {
            1: 10,
            2: 5,
            3: 2,
            4: 1,
            10: 1
        }
        self.assertEqual(size_adjacency_list(degree_distribution=degree_distribution, element_size=1), 40)
        self.assertEqual(size_adjacency_list(degree_distribution=degree_distribution, element_size=32), 1280)

    def test_size_adjacency_map(self):
        degree_distribution = {
            1: 10,
            2: 5,
            3: 2,
            4: 1,
            10: 1
        }
        self.assertEqual(size_adjacency_map(degree_distribution=degree_distribution, element_size=1, nb_nodes=19), 59)
        self.assertEqual(size_adjacency_map(degree_distribution=degree_distribution, element_size=32, nb_nodes=19), 1888)


if __name__ == '__main__':
    unittest.main()
