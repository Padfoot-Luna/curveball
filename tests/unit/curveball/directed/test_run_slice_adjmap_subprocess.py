import unittest

from curveball.directed.run_sliced_adjmap_subprocess import run


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

        new_adjacency_list = run(adjacency_list=adjacency_list.copy(), nb_steps=1, nb_workers=1)

        self.assertEqual(len(new_adjacency_list), len(adjacency_list))
        self.assertDictEqual(new_adjacency_list, adjacency_list)

    def test_single_step(self):
        """
        We check the properties of the newly generated adjacency list (same number of nodes same degree...)
        """
        adjacency_list = {
            1: {1, 2},
            2: {2, 3},
            3: {3, 4},
            4: {4, 1}
        }

        for i in range(10):
            with self.subTest(i=i):
                new_adjacency_list = run(adjacency_list=adjacency_list.copy(), nb_steps=1, nb_workers=2)

                self.assertEqual(len(new_adjacency_list), 4)
                self.assertEqual(len(new_adjacency_list[1]), 2)
                self.assertEqual(len(new_adjacency_list[2]), 2)
                self.assertEqual(len(new_adjacency_list[3]), 2)
                self.assertEqual(len(new_adjacency_list[4]), 2)


if __name__ == '__main__':
    unittest.main()
