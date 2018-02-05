import unittest

from curveball.classical.run import step


class TestCurveballBipartite(unittest.TestCase):
    def test_fixed_point(self):
        """
        Here we provide the adjacency list from an all to all connected graph
        We expect that the curveball algorithm will return the same adjacency list as the input
        """
        adjacency_list = [
            (1, {10, 20, 30}),
            (2, {10, 20, 30}),
            (3, {10, 20, 30})
        ]

        new_adjacency_list = step(adjacency_list.copy())
        self.assertEqual(len(adjacency_list), len(new_adjacency_list))
        for line in adjacency_list:
            self.assertIn(line, new_adjacency_list)

    def test_single_step(self):
        """
        We check the properties of the newly generated adjacency list (same number of nodes same degree...)
        """
        adjacency_list = [
            (1, {10, 20}),
            (2, {20, 30}),
            (3, {30, 40}),
            (4, {40, 10})
        ]

        for i in range(1000):
            with self.subTest(i=i):
                new_adjacency_list = step(adjacency_list.copy())
                self.assertEqual(len(adjacency_list), len(new_adjacency_list))
                for node, neighbors in new_adjacency_list:
                    self.assertIn(node, range(1, 5))
                    self.assertEqual(len(neighbors), 2)


if __name__ == '__main__':
    unittest.main()