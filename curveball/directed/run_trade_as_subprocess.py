# -*- coding: utf-8 -*-
from multiprocessing.pool import Pool
from random import shuffle
from typing import Dict

from curveball.core import trade_without_self_loop


def step(adjacency_list: Dict[int, set], pool: Pool) -> Dict[int, set]:
    """
    Runs one step:
    1. prepare all pair of nodes and their corresponding neighborhood
    2. for each pair of nodes (and their corresponding neighborhood), run the trade in parallel
    3. wait for every thread to finish and recompose the new adjacency list from the obtained trades

    :param pool: the thread pool object
    :param adjacency_list: the graph adjacency list
    :return: a new adjacency list generated thanks to the curveball algorithm
    """
    nodes = list(adjacency_list.keys())
    shuffle(nodes)

    kwargs = [
        (
            nodes[i - 1],
            adjacency_list[nodes[i - 1]],
            nodes[i], adjacency_list[nodes[i]]
        )
        for i in range(1, len(nodes), 2)
    ]

    # run the trades in parallel (this will result in list of trades)
    trades = pool.starmap(trade_without_self_loop, kwargs)

    # recompose the new adjacency list
    for trade in trades:
        for k, v in trade.items():
            adjacency_list[k] = v

    return adjacency_list

def run(adjacency_list: Dict, nb_steps: int, nb_workers: int) -> Dict:
    """
    Runs a certain number of steps
    :param nb_workers: number of threads to work in parallel
    :param adjacency_list: the starting adjacency list
    :param nb_steps: the number of steps to run
    :return: a new adjacency list
    """
    with Pool(nb_workers) as pool:
        for _ in range(nb_steps):
            adjacency_list = step(adjacency_list, pool)
    return adjacency_list
