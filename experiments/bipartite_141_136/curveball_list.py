import cProfile
import os
import random
from memory_profiler import profile
import psutil

from utilities.load_save_data import read_csv_list, save_csv_list
from curveball.classical.run import step, run
import curveball.classical.run_subprocess as subpro


def step_list(nb_samples: int):
    adj_list = read_csv_list(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    seed = 0
    random.seed(seed)
    for i in range(nb_samples):
        adj_list = step(adjacency_list=adj_list)
        save_csv_list(adjacency_list=adj_list,
                      filename=os.path.join(os.path.dirname(__file__), 'data/step_seed{}_step{}.csv'.format(seed, i)))


def run_list(nb_samples: int):
    adj_list = read_csv_list(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    random.seed(0)
    for i in range(1, nb_samples+1):
        adj_list = run(adjacency_list=adj_list, nb_steps=10)
        save_csv_list(adjacency_list=adj_list,
                      filename=os.path.join(os.path.dirname(__file__), 'data/run_seed{}_step{}.csv'.format(0, i)))


def parallel_run(nb_samples: int):
    adj_list = read_csv_list(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    for i in range(nb_samples):
        random.seed(i)
        adj_list = subpro.run(adjacency_list=adj_list, nb_steps=10, nb_workers=3)
        save_csv_list(adjacency_list=adj_list, filename=os.path.join(os.path.dirname(__file__),
                                                                     'data/subprocess_run_seed{}_step{}.csv'
                                                                     .format(i, 9)))


def main():
    step_list(100)
    run_list(100)
    parallel_run(100)


if __name__ == '__main__':
    cProfile.run('main()')



