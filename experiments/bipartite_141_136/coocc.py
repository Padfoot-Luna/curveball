import cProfile
import os

from utilities.load_save_data import read_csv
from metrics.cooccurrence import compute_cooccurrence_graph, cooccurrence_set_operation


def is_statistically_significant(adjacency_map, index_node_1, index_node_2, p):
    p_value = 0
    coocc = []
    coocc[0] = cooccurrence_set_operation(index_node_1, index_node_2, adjacency_list=adjacency_map)
    for i in range(1, 11):
        with open('data/coocc_step_{}.csv'.format(i), 'r') as f:
            data = f.readline(index_node_1).split('{')
            data = data[1].split('}')
            data = data.split(':')
            coocc[i] = data[index_node_2 - index_node_1 - 1]
        if coocc[i] > coocc[0]:
            p_value += 1
    if p_value/10 < p:
        return True
    else:
        return False


def main():
    # G_0: 1. read_csv->Dict[int,set]   2.degree sequence->Dict[int,int]   3.coocc
    adjacency_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))

    fixed_degree_sequence = {}
    # for node, neighbors in adjacency_map.items():
    #     fixed_degree_sequence[node] = len(neighbors)
    # more efficient ->?
    for node in adjacency_map:
        fixed_degree_sequence[node] = len(adjacency_map[node])

    coocc = compute_cooccurrence_graph(adjacency_list=adjacency_map)
    with open(os.path.join(os.path.dirname(__file__), 'data/coocc_step_0.csv'), 'w') as f:
        for node in list(adjacency_map.keys())[:-1]:
            f.write('{}:{}\n'.format(node, coocc[node]))

    # G_1-G_10: 1.read_csv->Dict[int,set]    2.coocc
    for i in range(1, 3):
        adj_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/run_seed0_step{}.csv'.format(i)))
        coocc = compute_cooccurrence_graph(adjacency_list=adj_map)
        with open(os.path.join(os.path.dirname(__file__), 'data/coocc_step_{}.csv'.format(i)), 'w') as f:
            for node in list(adjacency_map.keys())[:-1]:
                f.write('{}:{}\n'.format(node, coocc[node]))

    # stats






if __name__ == '__main__':
    cProfile.run('main()')




