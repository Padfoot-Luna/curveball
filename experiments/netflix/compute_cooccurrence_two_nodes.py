import cProfile
import os
import random

from curveball.classical.run import step
from metrics.cooccurrence import cooccurrence_set_operation
from utilities.load_save_data import read_csv


def sample_nodes_with_degree_d(adjacency_list, degree=10, nb_sample=10):
    nodes_with_given_degree = [node for node, neighbors in adjacency_list.items() if len(neighbors) == degree]
    if len(nodes_with_given_degree) > nb_sample:
        return [nodes_with_given_degree.pop(random.randint(0, len(nodes_with_given_degree) - 1)) for _ in range(nb_sample)]
    return nodes_with_given_degree


def compute_sample_coocc(adjacency_list, d10, d100, d1000):
    coocc = []
    coocc += [(n1, n2, 10, 10, cooccurrence_set_operation(adjacency_list=adjacency_list, index_node1=n1, index_node2=n2)) for n1 in d10
              for n2 in d10 if n2 > n1]
    coocc += [(n1, n2, 100, 100, cooccurrence_set_operation(adjacency_list=adjacency_list, index_node1=n1, index_node2=n2)) for n1 in
              d100 for n2 in d100 if n2 > n1]
    coocc += [(n1, n2, 1000, 1000, cooccurrence_set_operation(adjacency_list=adjacency_list, index_node1=n1, index_node2=n2)) for n1 in
              d1000 for n2 in d1000 if n2 > n1]
    coocc += [(n1, n2, 10, 100, cooccurrence_set_operation(adjacency_list=adjacency_list, index_node1=n1, index_node2=n2)) for n1 in
              d10 for n2 in d100]
    coocc += [(n1, n2, 10, 1000, cooccurrence_set_operation(adjacency_list=adjacency_list, index_node1=n1, index_node2=n2)) for n1 in
              d10 for n2 in d1000]
    coocc += [(n1, n2, 100, 1000, cooccurrence_set_operation(adjacency_list=adjacency_list, index_node1=n1, index_node2=n2)) for n1 in
              d100 for n2 in d1000]
    return coocc


def main():
    filename = '/home/julien/Documents/SPPII/data/Netflix_20k/Netflix_Dataset_Good_20k.csv'
    random.seed(0)
    adjacency_list = read_csv(filename=filename)

    d10 = sample_nodes_with_degree_d(adjacency_list, degree=10, nb_sample=10)
    d100 = sample_nodes_with_degree_d(adjacency_list, degree=100, nb_sample=10)
    d1000 = sample_nodes_with_degree_d(adjacency_list, degree=1000, nb_sample=10)

    coocc = compute_sample_coocc(adjacency_list, d10, d100, d1000)

    with open(os.path.join(os.path.dirname(__file__), 'data/coocc_step_0.csv'), 'w') as f:
        f.write('\n'.join([','.join([str(x) for x in c]) for c in coocc]))

    for i in range(100):
        # Compute the curveball
        adjacency_list = step(adjacency_list)

        coocc = compute_sample_coocc(adjacency_list, d10, d100, d1000)

        with open(os.path.join(os.path.dirname(__file__), 'data/coocc_step_{}.csv'.format(i + 1)), 'w') as f:
            f.write('\n'.join([','.join([str(x) for x in c]) for c in coocc]))


if __name__ == '__main__':
    cProfile.run('main()')
