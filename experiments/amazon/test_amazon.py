# -*- coding: utf-8 -*-

import cProfile
import os
import random

from curveball.classical.run import step
from utilities.load_save_data import read_csv, save_csv


def main():
    dataset = '/home/julien/Documents/SPPII/data/Amazon/adj-map-amazon0302.csv'
    adjacency_list = read_csv(filename=dataset)
    seed = 0
    random.seed(seed)
    for i in range(10):
        adjacency_list = step(adjacency_list)
        save_csv(adjacency_list=adjacency_list, filename=os.path.join(os.path.dirname(__file__), 'data/amazon_step_seed{}_step{}.csv'.format(seed, i)))


if __name__ == '__main__':
    cProfile.run('main()')