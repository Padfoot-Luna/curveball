import random
import unittest
from multiprocessing.pool import ThreadPool

from curveball.classical.run_trade_as_thread import step


class TestCurveballClassical(unittest.TestCase):
    def test_fixed_point(self):
        """
        Here we provide the adjacency list from an all to all connected graph
        We expect that the curveball algorithm will return the same adjacency list as the input
        """
        adjacency_list = {
            1: {1, 2, 3},
            2: {1, 2, 3},
            3: {1, 2, 3}
        }

        pool = ThreadPool(2)

        new_adjacency_list = step(adjacency_list, pool)

        self.assertEqual(len(new_adjacency_list), len(adjacency_list))
        self.assertDictEqual(new_adjacency_list, adjacency_list)

    def test_single_step(self):
        """
        We check the properties of the newly generated adjacency list (same number of nodes same degree...)
        """
        random.seed(0)

        pool = ThreadPool(2)

        adjacency_list = {
            1: {2},
            2: {3},
            3: {4},
            4: {5},
            5: {6},
            6: {1}
        }

        for i in range(1000):
            with self.subTest(i=i):
                new_adjacency_list = step(adjacency_list, pool)

                self.assertEqual(len(new_adjacency_list), 6)
                self.assertEqual(len(new_adjacency_list[1]), 1)
                self.assertEqual(len(new_adjacency_list[2]), 1)
                self.assertEqual(len(new_adjacency_list[3]), 1)
                self.assertEqual(len(new_adjacency_list[4]), 1)
                self.assertEqual(len(new_adjacency_list[5]), 1)
                self.assertEqual(len(new_adjacency_list[6]), 1)


if __name__ == '__main__':
    unittest.main()
