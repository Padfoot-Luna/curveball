# -*- coding: utf-8 -*-

import random
import unittest
from multiprocessing.pool import Pool

from curveball.classical.run_subprocess import parallel_step


class TestCurveballClassical(unittest.TestCase):
    def test_fixed_point(self):
        """
        Here we provide the adjacency list from an all to all connected graph
        We expect that the curveball algorithm will return the same adjacency list as the input
        """
        adjacency_list = [
            (1, {1, 2, 3}),
            (2, {1, 2, 3}),
            (3, {1, 2, 3})
        ]

        pool = Pool(2)

        new_adjacency_list = parallel_step(adjacency_list, n=3, nb_workers=2, pool=pool)

        self.assertEqual(new_adjacency_list, adjacency_list)

    def test_single_step(self):
        """
        We check the properties of the newly generated adjacency list (same number of nodes same degree...)
        """
        random.seed(0)

        pool = Pool(2)

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
                new_adjacency_list = parallel_step(adjacency_list, n=6, nb_workers=2, pool=pool)

                self.assertEqual(len(new_adjacency_list), 6)
                self.assertEqual(len(new_adjacency_list[0][1]), 1)
                self.assertEqual(len(new_adjacency_list[1][1]), 1)
                self.assertEqual(len(new_adjacency_list[2][1]), 1)
                self.assertEqual(len(new_adjacency_list[3][1]), 1)
                self.assertEqual(len(new_adjacency_list[4][1]), 1)
                self.assertEqual(len(new_adjacency_list[5][1]), 1)


if __name__ == '__main__':
    unittest.main()
