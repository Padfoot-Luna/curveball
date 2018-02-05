# -*- coding: utf-8 -*-

"""
Profiling Curveball implementation for directed graphs with self loops
or bipartite graphs (single thread implementation)


Run this file with cProfile option, e.g.

```bash
python -m cProfile profile_run.py --dataset=PATH/TO/YOUR/DATA --steps=10000 > SOME_OUTPUT_FILE.txt
```

https://docs.python.org/3/library/profile.html
"""

import argparse
import os

from curveball.classical.run import run
from utilities.load_save_data import read_csv_list


def main(filename: str, steps: int):
    """

    :param filename: a filename to read for loading the adjacency list
    :param steps: the number of steps to perform in the curveball algorithm
    :return:
    """
    adjacency_list = read_csv_list(filename)
    run(adjacency_list, nb_steps=steps)


if __name__ == '__main__':
    default_dataset = os.path.join(os.path.dirname(__file__), '../default_datasets/bipartite.csv')
    parser = argparse.ArgumentParser(
        description='Profiling Curveball implementation for directed graphs with self loops '
                    'or bipartite graphs (single thread implementation)')
    parser.add_argument('--dataset', type=str, help='The adjacency map file to load', default=default_dataset)
    parser.add_argument('--steps', type=int, help='The number of steps of the curveball algorithm to run', default=10)
    args = parser.parse_args()
    main(filename=args.dataset, steps=args.steps)
