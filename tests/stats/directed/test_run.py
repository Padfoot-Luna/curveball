import random
import unittest
from collections import defaultdict

from scipy.stats import chisquare, chi2

from curveball.directed.run import run
from tests.datasets.directed.dataset import a_directed_graph
from tests.utils import to_unique_string
from utilities.networkx import is_isomorphic, create_networkx_digraph


class TestCurveballDirected(unittest.TestCase):
    def test_run_is_uar(self):
        """
        Running the curveball algorithm on a small graph space (only two expected adjacency lists)
        """
        random.seed(0)

        # number of samples
        n = 1000

        # starting adjacency list
        adjacency_list = a_directed_graph[0]

        # sampling
        adjacency_lists = defaultdict(int)
        adjacency_lists[to_unique_string(adjacency_list)] += 1
        for _ in range(n):
            adjacency_lists[to_unique_string(run(adjacency_list, 100))] += 1

        # each unique item shall appear with the following frequency / nb of appearance
        expected_frequency = 1. / len(adjacency_lists)
        expected_nb = int(n * expected_frequency)

        # compute chi square statistics
        error_squared = {k: (v - expected_nb) ** 2 / expected_nb for k, v in adjacency_lists.items()}
        my_chi_square = sum(v for _, v in error_squared.items())
        # degree of freedom = number of variable categories - 1
        df = len(adjacency_lists) - 1
        # critical value for 95% confidence*
        crit = chi2.ppf(q=0.95, df=df)
        # p-value
        my_p_value = 1 - chi2.cdf(x=my_chi_square, df=df)

        # do the same with scipy (one never knows...)
        scipy_chi_square, scipy_p_value = chisquare(f_obs=[v for _, v in adjacency_lists.items()], f_exp=expected_nb,
                                                    ddof=0, axis=0)

        # test our differences scipy and I
        self.assertAlmostEqual(scipy_chi_square, my_chi_square)
        self.assertAlmostEqual(scipy_p_value, my_p_value)

        # here is the real statistical test
        # if this pass, we are sure (with 0.95% confidence) that our null hypothesis is valid:
        # i.e., our sample of randomly chosen items is done uniformly
        self.assertLess(my_chi_square, crit)
        self.assertGreater(my_p_value, 0.05)

    def test_run_for_completeness(self):
        """
        For a given graph distribution (small enough), we generated the full space of possible graphs,
        then checks whether the curveball algorithm generates all possible graphs
        """
        random.seed(0)

        # number of samples
        n = 5000

        starting_adj_list = a_directed_graph[0]

        expected_adjacency_lists = a_directed_graph

        # sampling
        graphs = [create_networkx_digraph(starting_adj_list)]
        for _ in range(n):
            adjacency_list = run(starting_adj_list, 100)
            graph = create_networkx_digraph(adjacency_list)
            if not is_isomorphic(g=graph, graphs=graphs):
                graphs.append(graph)

        self.assertEqual(len(expected_adjacency_lists), len(graphs))


if __name__ == '__main__':
    unittest.main()
