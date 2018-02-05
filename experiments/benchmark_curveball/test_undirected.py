import cProfile

from curveball.undirected.run import run
from tests.datasets.undirected.dataset import an_undirected_graph


def main():
    adjacency_list = an_undirected_graph[0]
    run(adjacency_list, nb_steps=1000)


if __name__ == '__main__':
    cProfile.run('main()')
