import cProfile

from curveball.directed.run import run
from tests.datasets.directed.dataset import a_directed_graph


def main():
    adjacency_list = a_directed_graph[0]
    run(adjacency_list, nb_steps=1000)


if __name__ == '__main__':
    cProfile.run('main()')
