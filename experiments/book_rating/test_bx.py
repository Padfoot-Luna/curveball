# -*- coding: utf-8 -*-

import cProfile
import os
import random

from curveball.classical.run import step


def read_csv(filename):
    """
    Read an adjacency map from a file with the following format

    node1:neighbor1,neighbor2,neighbor3...
    node2:neighbor1,neighbor2,neighbor3...

    :param filename:
    :return: adjacency_list
    """
    i = 0
    adjacency_list = {}
    with open(filename, 'r') as f:
        for line in f:
            i += 1
            try:
                node, neighbors = line.strip().split('|')
                adjacency_list[int(node)] = set(neighbors.split(','))
            except ValueError:
                print(i,line)
    return adjacency_list

def save_csv(adjacency_list, filename):
    """
    Save an adjacency map to a file with the following format

    node1:neighbor1,neighbor2,neighbor3...
    node2:neighbor1,neighbor2,neighbor3...

    :param adjacency_list:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        for k, v in adjacency_list.items():
            f.write('{}|{}\n'.format(k, ','.join([str(x) for x in v])))

def main():
    # Dataset from http://www2.informatik.uni-freiburg.de/~cziegler/BX/
    dataset = '/home/julien/Documents/SPPII/data/BX/Adjacency-Map-Book-Ratings.csv'
    adjacency_list = read_csv(filename=dataset)
    seed = 0
    random.seed(seed)
    for i in range(10):
        adjacency_list = step(adjacency_list)
        save_csv(adjacency_list=adjacency_list, filename=os.path.join(os.path.dirname(__file__), 'data/BX_step_seed{}_step{}.csv'.format(seed, i)))


if __name__ == '__main__':
    cProfile.run('main()')