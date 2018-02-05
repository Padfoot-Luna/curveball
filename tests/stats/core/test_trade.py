import unittest
from collections import Counter

from scipy.stats import chisquare, chi2

from curveball.core import trade_with_self_loop, trade_without_self_loop


class TestSelectNodes(unittest.TestCase):
    def test_trade_with_self_loop(self):
        """
        checking that calling trade_trade_with_self_loop several times
        returns all possible trades uniformly at random
        (thanks to Chi Square test)

        Given two nodes n1 and n2 with independent neighborhoods (non intersecting sets),
        e.g., neighborhood of n1 = {1, 2} and neighborhood of n2 = {3, 4}
        Then the trade algorithm shall produce new neighbors for n1 and n2 that can be all combinations of 1,2,3,4
        e.g., {1, 2}, {3, 4}, {1, 3}, {2, 4}, {1, 4}, {2, 3}
        Each can be a new neighborhood of either n1 or n2 with the same probability 1/3

        Let l the length of the number of possible new neighborhoods (here it is l=6),
        calling the function trade_neighbors N times, one shall see each new neighborhood appearing with a frequency 2/l:
        """
        new_neighbors_obtained = []

        # number of samples
        n = 10000

        # set of neighbors to start with
        neighbors_node_1 = {1, 2}
        neighbors_node_2 = {3, 4}

        # all possible new neighbors combinations.
        # Since both nodes have the same number of neighbours and
        # since the interstection of their neighborhood is empty
        # one can simplify the test by considering all combinations with the same probability
        possible_neighbors = [{1, 2}, {3, 4}, {1, 3}, {2, 4}, {1, 4}, {2, 3}]

        # each unique item shall appear with the following frequency / nb of appearance
        expected_frequency = 2. / len(possible_neighbors)
        expected_nb = int(n * expected_frequency)

        # sampling
        for i in range(n):
            # compute the new neighbors
            trade = trade_with_self_loop(index_node_1=1,
                                         index_node_2=2,
                                         neighbors_node_1=neighbors_node_1,
                                         neighbors_node_2=neighbors_node_2)
            new_neighbors_node_1 = trade[0][1]
            new_neighbors_node_2 = trade[1][1]
            # make the set hashable so we can use Counter to count how many of them are here
            new_neighbors_obtained += [str(new_neighbors_node_1), str(new_neighbors_node_2)]

        # count appearance of each unique item
        c = Counter(new_neighbors_obtained)

        # compute chi square statistics
        error_squared = {k: (v - expected_nb) ** 2 / expected_nb for k, v in c.items()}
        my_chi_square = sum(v for _, v in error_squared.items())
        # degree of freedom = number of variable categories - 1
        df = len(possible_neighbors) - 1
        # critical value for 95% confidence*
        crit = chi2.ppf(q=0.95, df=df)
        # p-value
        my_p_value = 1 - chi2.cdf(x=my_chi_square, df=df)

        # do the same with scipy (one never knows...)
        scipy_chi_square, scipy_p_value = chisquare(f_obs=[v for _, v in c.items()], f_exp=expected_nb, ddof=0,
                                                    axis=0)

        # test our differences scipy and I
        self.assertAlmostEqual(scipy_chi_square, my_chi_square)
        self.assertAlmostEqual(scipy_p_value, my_p_value)

        # here is the real statistical test
        # if this pass, we are sure (with 0.95% confidence) that our null hypothesis is valid:
        # i.e., our sample of randomly chosen items is done uniformly
        self.assertLess(my_chi_square, crit)
        self.assertGreater(my_p_value, 0.05)

    def test_trade_without_self_loop(self):
        """
        checking that calling trade_trade_without_self_loop several times
        returns all possible trades uniformly at random
        (thanks to Chi Square test)

        Given two nodes n1 and n2 with independent neighborhoods (non intersecting sets),
        e.g., neighborhood of n1 = {3, 4} and neighborhood of n2 = {5, 6}
        Then the trade algorithm shall produce new neighbors for n1 and n2 that can be all combinations of 3,4,5,6
        e.g., {3, 4}, {3, 5}, {3, 6}, {4, 5}, {4, 6}, {5, 6}
        Each can be a new neighborhood of either n1 or n2 with the same probability 1/3

        Let l the length of the number of possible new neighborhoods (here it is l=6),
        calling the function trade_neighbors N times, one shall see each new neighborhood appearing with a frequency 2/l:
                """

        # number of samples
        n = 10000

        dataset = [
            {
                'neighbors_node_1': {3, 4},
                'neighbors_node_2': {5, 6},
                'possible_neighbors': [{3, 4}, {3, 5}, {3, 6}, {4, 5}, {4, 6}, {5, 6}],
            }, {
                'neighbors_node_1': {1, 3},
                'neighbors_node_2': {2, 4},
                'possible_neighbors': [{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}],
            }
        ]

        for test_data in dataset:
            with self.subTest(test_data=test_data):
                new_neighbors_obtained = []
                neighbors_node_1 = test_data['neighbors_node_1']
                neighbors_node_2 = test_data['neighbors_node_2']
                possible_neighbors = test_data['possible_neighbors']

                # each unique item shall appear with the following frequency / nb of appearance
                expected_frequency = 2. / len(possible_neighbors)
                expected_nb = int(n * expected_frequency)

                # sampling
                for i in range(n):
                    # compute the new neighbors
                    trade = trade_without_self_loop(index_node_1=1,
                                                    neighbors_node_1=neighbors_node_1,
                                                    index_node_2=2,
                                                    neighbors_node_2=neighbors_node_2)
                    new_neighbors_node_1 = trade[0][1]
                    new_neighbors_node_2 = trade[1][1]
                    # make the set hashable so we can use Counter to count how many of them are here
                    new_neighbors_obtained += [str(new_neighbors_node_1), str(new_neighbors_node_2)]

                # count appearance of each unique item
                c = Counter(new_neighbors_obtained)

                # compute chi square statistics
                error_squared = {k: (v - expected_nb) ** 2 / expected_nb for k, v in c.items()}
                my_chi_square = sum(v for _, v in error_squared.items())
                # degree of freedom = number of variable categories - 1
                df = len(possible_neighbors) - 1
                # critical value for 95% confidence*
                crit = chi2.ppf(q=0.95, df=df)
                # p-value
                my_p_value = 1 - chi2.cdf(x=my_chi_square, df=df)

                # do the same with scipy (one never knows...)
                scipy_chi_square, scipy_p_value = chisquare(f_obs=[v for _, v in c.items()], f_exp=expected_nb, ddof=0,
                                                            axis=0)

                # test our differences scipy and I
                self.assertAlmostEqual(scipy_chi_square, my_chi_square)
                self.assertAlmostEqual(scipy_p_value, my_p_value)

                # here is the real statistical test
                # if this pass, we are sure (with 0.95% confidence) that our null hypothesis is valid:
                # i.e., our sample of randomly chosen items is done uniformly
                self.assertLess(my_chi_square, crit)
                self.assertGreater(my_p_value, 0.05)


if __name__ == '__main__':
    unittest.main()
