import random
import unittest

from curveball.parutils import random_slice


class MyTestCase(unittest.TestCase):
    def test_random_slice(self):
        """
        Each element belongs to only one slice,
        The number of slices is fixed,
        At max, one slice has an odd number of elements
        """
        random.seed(0)
        adjacency_list = [
            (1, {2, 3, 6, 8}),
            (2, {5, 8, 9, 10}),
            (3, {1, 4, 6, 8}),
            (4, {2, 7, 8, 9, 10}),
            (5, {1, 2, 4, 7, 9}),
            (6, {3, 7}),
            (7, {8}),
            (8, {1, 2, 4, 5, 6, 8}),
            (9, {1, 5, 10}),
            (10, {1, 4, 8})
        ]

        slices = random_slice(adjacency_list, n=3)

        # test number of slices
        self.assertEqual(len(slices), 3)

        # test each slice contains element
        for x in adjacency_list:
            self.assertEqual(sum([x in slices[0], x in slices[1], x in slices[2]]), 1)


if __name__ == '__main__':
    unittest.main()
