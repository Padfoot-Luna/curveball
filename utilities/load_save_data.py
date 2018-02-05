import json
import pickle
from collections import defaultdict
from typing import List, Tuple, Dict


def extract_degree_sequence(edge_list_filename, sep=' '):
    """
    extract the degree sequence from a global edge list

    example:

    1 -- 10
    1 -- 11
    2 -- 11
    1 -- 12
    3 -- 12

    will end up in

    {1:3, 2:1, 3:1}, {10:1, 11:2, 12:2}

    :param edge_list_filename: the path to a file containing a global edge list (format should be 'node separator node')
    :param sep: separator (single character)
    :return: degrees_left: dict(int -> int), degrees_right: dict(int -> int)
    """

    degrees_left = defaultdict(int)
    degrees_right = defaultdict(int)
    with open(edge_list_filename, 'r') as f:
        for line in f:
            # skipping lines starting with #
            if line[0] == '#':
                continue
            source, target = line.strip().split(sep)
            degrees_left[int(source)] += 1
            degrees_right[int(target)] += 1
    return degrees_left, degrees_right


def extract_adjacency_list(edge_list_filename, sep=' '):
    """
    extract an adjacency map from a global edge list

    example:

    1 -- A
    1 -- B
    2 -- B
    1 -- C
    3 -- C

    will end up in

    1:A,B,C
    2:B
    3:C

    :param edge_list_filename: the path to a file containing a global edge list (format should be 'node separator node')
    :param sep: separator (single character)
    :return: adjacency_map (node -> [list of neighbors])
    """
    adjacency_list = defaultdict(set)
    with open(edge_list_filename, 'r') as f:
        for line in f:
            source, target = line.strip().split(sep)
            adjacency_list[int(source)].add(int(target))
    return adjacency_list


def extract_adjacency_list_right(edge_list_filename, sep=' '):
    """
    extract an adjacency map from a global edge list, using target nodes as source

    example:

    1 -- A
    1 -- B
    2 -- B
    1 -- C
    3 -- C

    will end up in

    A:1
    B:1,2
    C:1,3

    :param edge_list_filename:
    :param sep:
    :return:
    """
    adjacency_list = defaultdict(set)
    with open(edge_list_filename, 'r') as f:
        for line in f:
            source, target = line.strip().split(sep)
            adjacency_list[int(target)].add(int(source))
    return adjacency_list


def save_csv(adjacency_list: Dict[int, set], filename: str):
    """
    Save an adjacency map to a file with the following format

    node1:neighbor1,neighbor2,neighbor3...
    node2:neighbor1,neighbor2,neighbor3...

    :param adjacency_list:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        for k, v in adjacency_list.items():
            f.write('{}:{}\n'.format(k, ','.join([str(x) for x in v])))


def save_csv_list(adjacency_list: List[Tuple[int, set]], filename: str):
    """
    Save an adjacency list to a file with the following format

    node1:neighbor1,neighbor2,neighbor3...
    node2:neighbor1,neighbor2,neighbor3...

    :param adjacency_list:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        for node, neighbors in adjacency_list:
            f.write('{}:{}\n'.format(node, ','.join([str(neighbor) for neighbor in neighbors])))


def read_csv(filename: str) -> Dict[int, set]:
    """
    Read an adjacency map from a file with the following format

    node1:neighbor1,neighbor2,neighbor3...
    node2:neighbor1,neighbor2,neighbor3...

    :param filename:
    :return: adjacency_list
    """
    adjacency_list = {}
    with open(filename, 'r') as f:
        for line in f:
            node, neighbors = line.strip().split(':')
            adjacency_list[int(node)] = set([int(x) for x in neighbors.split(',')])
    return adjacency_list


def read_csv_list(filename: str) -> List[Tuple[int, set]]:
    """
    Read an adjacency map from a file with the following format

    node1:neighbor1,neighbor2,neighbor3...
    node2:neighbor1,neighbor2,neighbor3...

    :param filename:
    :return: adjacency_list
    """
    adjacency_list = []
    with open(filename, 'r') as f:
        for line in f:
            node, neighbors = line.strip().split(':')
            adjacency_list += [(int(node), set([int(x) for x in neighbors.split(',')]))]
    return adjacency_list


def save_pickle(adjacency_list, filename):
    with open(filename, 'wb') as f:
        pickle.dump(adjacency_list, f, protocol=pickle.HIGHEST_PROTOCOL)


def read_pickle(filename):
    with open(filename, 'rb') as f:
        adjacency_list = pickle.load(f)
    return adjacency_list


def save_json(adjacency_list, filename):
    """
    Save an adjacency map to a json file

    :param adjacency_list:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        json.dump(adjacency_list, f)


def degree_from_adjacency_map_csv(filename):
    """
    Read an adjacency map csv file line by line and yield the node and its corresponding degree
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        for line in f:
            node, neighbors = line.strip().split(':')
            yield node, len(neighbors.split(','))


def read_csv_line(filename, node_index):
    """

    :param filename:
    :param node_index:
    :return:
    """
    with open(filename, 'r') as f:
        for line in f:
            node, neighbors = line.strip().split(':')
            if int(node) == node_index:
                return {int(node): {int(n) for n in neighbors.split(',')}}
