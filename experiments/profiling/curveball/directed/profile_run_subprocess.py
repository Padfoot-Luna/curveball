# -*- coding: utf-8 -*-

"""
Profiling Curveball implementation for directed graphs without self loops
where each parallel process is doing trades for a subset of the adjacency list

Run this file with cProfile option, e.g.

```bash
python -m cProfile profile_run.py --dataset=PATH/TO/YOUR/DATA --steps=10000 --workers=5 > SOME_OUTPUT_FILE.txt
```

https://docs.python.org/3/library/profile.html
"""

import argparse
import os

from curveball.directed.run_subprocess import run
from utilities.load_save_data import read_csv_list


def main(filename, steps, workers):
    adjacency_list = read_csv_list(filename)
    run(adjacency_list, nb_steps=steps, nb_workers=workers)


if __name__ == '__main__':
    default_dataset = os.path.join(os.path.dirname(__file__), '../default_datasets/directed.csv')
    parser = argparse.ArgumentParser(
        description='Profiling Curveball implementation for directed graphs without self loops'
                    'where each parallel process is doing trades for a subset of the adjacency list')
    parser.add_argument('--dataset', type=str, help='The adjacency map file to load', default=default_dataset)
    parser.add_argument('--steps', type=int, help='The number of steps of the curveball algorithm to run', default=10)
    parser.add_argument('--workers', type=int, help='The number of parallel workers', default=2)
    args = parser.parse_args()
    main(filename=args.dataset, steps=args.steps, workers=args.workers)
