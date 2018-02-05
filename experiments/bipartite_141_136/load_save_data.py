import os
from collections import defaultdict
from utilities.load_save_data import save_csv


def extract_adjacency_list_right(edge_list_filename, sep=' '):
    adj_list = defaultdict(set)
    with open(edge_list_filename, 'r') as f:
        for line in f:
            if line[0] == '%':
                continue
            neighbors, node = line.strip().split(sep)
            adj_list[int(node)].add(int(neighbors))

    return adj_list


if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), 'data/out.brunson_revolution_revolution')
    adjacency_list = extract_adjacency_list_right(filename)
    save_csv(adjacency_list=adjacency_list, filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))


