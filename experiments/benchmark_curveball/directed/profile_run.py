# -*- coding: utf-8 -*-

"""
Profiling Curveball implementation for directed graphs (single thread implementation)
"""

import argparse
import os

from curveball.directed.run import run
from utilities.load_save_data import read_csv


def main(filename, steps):
    adjacency_list = read_csv(filename)
    run(adjacency_list, nb_steps=steps)


if __name__ == '__main__':
    default_dataset = os.path.join(os.path.dirname(__file__), '../default_datasets/directed.csv')
    parser = argparse.ArgumentParser(
        description='Profiling Curveball implementation for directed graphs (single thread implementation)')
    parser.add_argument('--dataset', type=str, help='The adjacency map file to load', default=default_dataset)
    parser.add_argument('--steps', type=int, help='The number of steps of the curveball algorithm to run', default=10)
    args = parser.parse_args()
    main(filename=args.dataset, steps=args.steps)
