import cProfile
from collections import defaultdict

from metrics.cooccurrence import cooccurrence_bipartite


def extract_adjacency_list(edge_list_filename, sep=' '):
    """
    Extract an adjacency list from a file that contains all edges
    Format of the file shall be:
    starting_node_index separator target_node_index

    :param edge_list_filename:
    :return:
    """
    adjacency_list = defaultdict(set)

    with open(edge_list_filename, 'r') as f:
        for line in f:
            source, target = line.strip().split(sep)
            adjacency_list[int(source)].add(int(target))

    return adjacency_list


def main():
    data_file = '/home/julien/Documents/SPPII/data/Netflix_20k/Netflix_Dataset_Good_20k.txt'
    adjacency_list = extract_adjacency_list(data_file)
    coocc_list = cooccurrence_bipartite(adjacency_list)


if __name__ == '__main__':
    cProfile.run('main()')