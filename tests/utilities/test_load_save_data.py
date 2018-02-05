import filecmp
import os
import unittest

from utilities.load_save_data import read_csv, save_csv, extract_adjacency_list, extract_adjacency_list_right, \
    read_csv_line, read_csv_list, save_csv_list, extract_degree_sequence


class MyTestCase(unittest.TestCase):
    def setUp(self):
        path_to_data = os.path.join(os.path.dirname(__file__), 'test_dataset/')
        self.file_to_read = os.path.join(path_to_data, 'read_adjacency_map.csv')
        self.file_to_save = os.path.join(path_to_data, 'save_adjacency_map.csv')
        self.edge_list_file = os.path.join(path_to_data, 'edge_list.csv')

    def tearDown(self):
        try:
            os.remove(self.file_to_save)
        except OSError:
            pass

    def test_read_adjacency_map(self):
        """
        Loads a csv file and compares the extracted adjacency list with the expected one
        """
        expected_adjacency_list = {
            1: {10, 11, 12},
            2: {12, 13},
            3: {15},
            4: {11, 13, 14, 15},
            5: {10, 12, 13, 15}
        }

        actual_adjacency_list = read_csv(filename=self.file_to_read)

        self.assertEqual(len(expected_adjacency_list), len(actual_adjacency_list))
        self.assertSequenceEqual(expected_adjacency_list[1], actual_adjacency_list[1])
        self.assertSequenceEqual(expected_adjacency_list[2], actual_adjacency_list[2])
        self.assertSequenceEqual(expected_adjacency_list[3], actual_adjacency_list[3])
        self.assertSequenceEqual(expected_adjacency_list[4], actual_adjacency_list[4])
        self.assertSequenceEqual(expected_adjacency_list[5], actual_adjacency_list[5])

    def test_save_adjacency_map(self):
        """
        Compares files produced by save method wth expected one
        """
        adjacency_list = {
            1: {10, 11, 12},
            2: {12, 13},
            3: {15},
            4: {11, 13, 14, 15},
            5: {10, 12, 13, 15}
        }
        save_csv(adjacency_list=adjacency_list, filename=self.file_to_save)
        self.assertTrue(filecmp.cmp(self.file_to_save, self.file_to_read))

    def test_extract_adjacency_list(self):
        """
        Checks the adjacency map extracted from an edge list file
        """
        expected_adjacency_list = {
            1: {10, 11, 12},
            2: {12, 13},
            3: {15},
            4: {11, 13, 14, 15},
            5: {10, 12, 13, 15}
        }
        actual_adjacency_list = extract_adjacency_list(edge_list_filename=self.edge_list_file, sep=' ')

        self.assertEqual(len(expected_adjacency_list), len(actual_adjacency_list))
        self.assertSequenceEqual(expected_adjacency_list[1], actual_adjacency_list[1])
        self.assertSequenceEqual(expected_adjacency_list[2], actual_adjacency_list[2])
        self.assertSequenceEqual(expected_adjacency_list[3], actual_adjacency_list[3])
        self.assertSequenceEqual(expected_adjacency_list[4], actual_adjacency_list[4])
        self.assertSequenceEqual(expected_adjacency_list[5], actual_adjacency_list[5])

    def test_extract_adjacency_list_right(self):
        """
        Checks the adjacency map (using target as source) extracted from an edge list file
        """
        expected_adjacency_list = {
            10: {1, 5},
            11: {1, 4},
            12: {1, 2, 5},
            13: {2, 4, 5},
            14: {4},
            15: {3, 4, 5}
        }
        actual_adjacency_list = extract_adjacency_list_right(edge_list_filename=self.edge_list_file, sep=' ')

        self.assertEqual(len(expected_adjacency_list), len(actual_adjacency_list))
        self.assertSequenceEqual(expected_adjacency_list[10], actual_adjacency_list[10])
        self.assertSequenceEqual(expected_adjacency_list[11], actual_adjacency_list[11])
        self.assertSequenceEqual(expected_adjacency_list[12], actual_adjacency_list[12])
        self.assertSequenceEqual(expected_adjacency_list[13], actual_adjacency_list[13])
        self.assertSequenceEqual(expected_adjacency_list[14], actual_adjacency_list[14])
        self.assertSequenceEqual(expected_adjacency_list[15], actual_adjacency_list[15])

    def test_read_csv_line(self):
        """
        Checks the ine extracted from an adjacency map file
        """
        expected_line = {4: {11, 13, 14, 15}}
        actual_line = read_csv_line(self.file_to_read, node_index=4)
        self.assertDictEqual(expected_line, actual_line)

    def test_read_csv_list(self):
        """
        Loads a csv file and compares the extracted adjacency list with the expected one
        """
        expected_adjacency_list = [
            (1, {10, 11, 12}),
            (2, {12, 13}),
            (3, {15}),
            (4, {11, 13, 14, 15}),
            (5, {10, 12, 13, 15})
        ]

        actual_adjacency_list = read_csv_list(filename=self.file_to_read)

        self.assertEqual(len(expected_adjacency_list), len(actual_adjacency_list))
        self.assertSequenceEqual(expected_adjacency_list[0], actual_adjacency_list[0])
        self.assertSequenceEqual(expected_adjacency_list[1], actual_adjacency_list[1])
        self.assertSequenceEqual(expected_adjacency_list[2], actual_adjacency_list[2])
        self.assertSequenceEqual(expected_adjacency_list[3], actual_adjacency_list[3])
        self.assertSequenceEqual(expected_adjacency_list[4], actual_adjacency_list[4])

    def test_save_csv_list(self):
        """
        Compares files produced by save method wth expected one
        """
        adjacency_list = [
            (1, {10, 11, 12}),
            (2, {12, 13}),
            (3, {15}),
            (4, {11, 13, 14, 15}),
            (5, {10, 12, 13, 15})
        ]
        save_csv_list(adjacency_list=adjacency_list, filename=self.file_to_save)
        self.assertTrue(filecmp.cmp(self.file_to_save, self.file_to_read))

    def test_extract_degree_sequence(self):
        """
        Extracts degree sequence from a file and compare with expected value
        """
        expected_degrees_left = {
            1: 3,
            2: 2,
            3: 1,
            4: 4,
            5: 4
        }
        expected_degrees_right = {
            10: 2,
            11: 2,
            12: 3,
            13: 3,
            14: 1,
            15: 3
        }
        degrees_left, degrees_right = extract_degree_sequence(self.edge_list_file)
        self.assertDictEqual(expected_degrees_left, degrees_left)
        self.assertDictEqual(expected_degrees_right, degrees_right)


if __name__ == '__main__':
    unittest.main()
