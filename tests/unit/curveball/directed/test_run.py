import unittest

from curveball.directed.run import step


class TestCurveballDirected(unittest.TestCase):
    def test_fixed_point(self):
        """
        Here we provide the adjacency list from an all to all connected graph
        We expect that the curveball algorithm will return the same adjacency list as the input
        """
        adjacency_list = [
            (1, {2, 3}),
            (2, {1, 3}),
            (3, {1, 2})
        ]

        new_adjacency_list = step(adjacency_list)

        self.assertListEqual(new_adjacency_list, adjacency_list)


    def test_single_step(self):
        """
        We check the properties of the newly generated adjacency list (same number of nodes same degree...)
        """
        adjacency_list = [
            (1, {2}),
            (2, {3}),
            (3, {4}),
            (4, {5}),
            (5, {6}),
            (6, {1})
        ]

        for i in range(1000):
            with self.subTest(i=i):
                new_adjacency_list = step(adjacency_list)

                self.assertEqual(len(new_adjacency_list), 6)
                for node, neighbors in new_adjacency_list:
                    self.assertIn(node, range(1,7))
                    self.assertEqual(len(neighbors), 1)


if __name__ == '__main__':
    unittest.main()
