from tests.datasets.classical.dataset import a_digraph_with_loops
from utilities.dot import undirected_graph_to_dot


def draw_undirected():
    for i, adjacency_list in enumerate(a_digraph_with_loops):
        with open('img/g{}.dot'.format(i), 'w') as f:
            f.write(undirected_graph_to_dot(adjacency_list=adjacency_list))


if __name__ == '__main__':
    draw_undirected()
