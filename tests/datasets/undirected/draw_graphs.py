from tests.datasets.undirected.dataset import an_undirected_graph
from utilities.dot import undirected_graph_to_dot


def draw_undirected():
    for i, adjacency_list in enumerate(an_undirected_graph):
        with open('img/g{}.dot'.format(i), 'w') as f:
            f.write(undirected_graph_to_dot(adjacency_list=adjacency_list))


if __name__ == '__main__':
    draw_undirected()
