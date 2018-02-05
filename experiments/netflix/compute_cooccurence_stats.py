# -*- coding: utf-8 -*-
import numpy as np
from collections import defaultdict


def get_nodes(deg1, deg2, coocc):
    return [k for k in coocc[0].keys() if k.split(',')[-2:] == [deg1, deg2]]


def get_cumulative_coocc_mean(deg1, deg2, nb_files, coocc):
    return [np.mean([[coocc[k][x] for x in get_nodes(deg1, deg2, coocc)] for k in range(i)]) for i in range(1, 100)]


def get_cumulative_coocc_std(deg1, deg2, nb_files, coocc):
    return [np.std([[coocc[k][x] for x in get_nodes(deg1, deg2, coocc)] for k in range(i)]) for i in range(1, 100)]


def get_coocc_from_files(nb_files):
    coocc = defaultdict(dict)
    for i in range(nb_files):
        with open('data/coocc_step_{}.csv'.format(i), 'r') as f:
            for line in f:
              data = line.strip().split(',')
              coocc[i][','.join(data[:-1])] = int(data[-1])
    return coocc


if __name__ == '__main__':
    coocc = get_coocc_from_files(100)
    degrees = ['10', '100', '1000']
    for i in range(len(degrees)):
        deg1 = degrees[i]
        for j in range(i, len(degrees)):
            deg2 = degrees[j]
            with open('sample_cum_cooc_deg_{}_{}.txt'.format(deg1, deg2), 'w') as f:
                f.write('AVG,STD\n')
                avg = get_cumulative_coocc_mean(deg1, deg2, nb_files=100, coocc=coocc)
                std = get_cumulative_coocc_std(deg1, deg2, nb_files=100, coocc=coocc)
                for i in range(len(avg)):
                    f.write('{},{}\n'.format(avg[i], std[i]))
