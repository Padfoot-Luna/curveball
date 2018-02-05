import cProfile
import os
import random
from memory_profiler import profile

from utilities.load_save_data import save_csv, read_csv
import curveball.classical.run_trade_as_thread as tt
import curveball.classical.run_trade_as_subprocess as ts
import curveball.classical.run_sliced_adjmap_thread as st
import curveball.classical.run_sliced_adjmap_subprocess as ss


def run_trade_as_thread(nb_samples: int):
    adj_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    for i in range(nb_samples):
        random.seed(i)
        adj_map = tt.run(adjacency_list=adj_map, nb_steps=10, nb_workers=3)
        save_csv(adjacency_list=adj_map, filename=os.path.join(os.path.dirname(__file__),
                                                               'data/trade_thread_seed{}_step{}.csv'.format(i, 9)))


def run_trade_as_subprocess(nb_samples: int):
    adj_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    for i in range(nb_samples):
        random.seed(i)
        adj_map = ts.run(adjacency_list=adj_map, nb_steps=10, nb_workers=3)
        save_csv(adjacency_list=adj_map, filename=os.path.join(os.path.dirname(__file__),
                                                               'data/trade_subprocess_seed{}_step{}.csv'.format(i, 9)))

def run_sliced_as_thread(nb_samples: int):
    adj_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    for i in range(nb_samples):
        random.seed(i)
        adj_map = st.run(adjacency_list=adj_map, nb_steps=10, nb_workers=3)
        save_csv(adjacency_list=adj_map, filename=os.path.join(os.path.dirname(__file__),
                                                               'data/sliced_thread_seed{}_step{}.csv'.format(i, 9)))


def run_sliced_as_subprocess(nb_samples: int):
    adj_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    for i in range(nb_samples):
        random.seed(i)
        adj_map = ss.run(adjacency_list=adj_map, nb_steps=10, nb_workers=3)
        save_csv(adjacency_list=adj_map, filename=os.path.join(os.path.dirname(__file__),
                                                               'data/sliced_subprocess_seed{}_step{}.csv'.format(i, 9)))


def main():
    '''
    adj_map = read_csv(filename=os.path.join(os.path.dirname(__file__), 'data/adj_list_right.csv'))
    for i in range(10):
        random.seed(i)
        adj_map = ts.run(adjacency_list=adj_map, nb_steps=10, nb_workers=3)
        save_csv(adjacency_list=adj_map, filename=os.path.join(os.path.dirname(__file__),
                                                               'data/trade_subprocess_seed{}_step{}.csv'.format(i, 9)))
    '''
    run_trade_as_thread(100)
    run_trade_as_subprocess(100)
    run_sliced_as_thread(100)
    run_sliced_as_subprocess(100)


if __name__ == '__main__':
    cProfile.run('main()')
