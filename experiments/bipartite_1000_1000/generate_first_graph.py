from fsdm.fsdm import generate_random_bipartite_graph
from utilities.load_save_data import save_csv
from utilities.havel_hakimi import iterative_check_hh_theorem

if __name__ == '__main__':
    with open('/home/julien/Documents/SPPII/data/random_bipartite_1000_1000_nodes/degree_sequence_left_1000_1000.csv',
              'r') as f:
        degree_sequence_left = [int(line.strip().split(',')[1]) for line in f]
    with open('/home/julien/Documents/SPPII/data/random_bipartite_1000_1000_nodes/degree_sequence_right_1000_1000.csv',
              'r') as f:
        degree_sequence_right = [int(line.strip().split(',')[1]) for line in f]
    assert len(degree_sequence_right) == len(degree_sequence_left) == 1000
    assert sum(degree_sequence_left) == sum(degree_sequence_right)

    assert iterative_check_hh_theorem(degree_sequence=degree_sequence_left + degree_sequence_right)

    adjacency_list = generate_random_bipartite_graph(degrees=degree_sequence_left + degree_sequence_right,
                                                     nb_nodes_left=len(degree_sequence_left))
    save_csv(adjacency_list=adjacency_list,
             filename='/home/julien/Documents/SPPII/data/random_bipartite_1000_1000_nodes/graph0.csv')
