from tests.datasets.directed.dataset import a_directed_graph
from utilities.dot import directed_graph_to_dot


def draw_undirected():
    for i, adjacency_list in enumerate(a_directed_graph):
        with open('img/g{}.dot'.format(i), 'w') as f:
            f.write(directed_graph_to_dot(adjacency_list=adjacency_list))


if __name__ == '__main__':
    draw_undirected()
