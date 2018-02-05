import random
import unittest
from collections import defaultdict

from curveball.core import trade_with_self_loop, trade_without_self_loop, exchange_neighbors


class TestTrade(unittest.TestCase):
    def test_no_possible_exchange(self):
        """
        No trades are possible,
        then function exchange_neighbors shall return
        the same neighbors sets as the ones given as input
        """
        neighbors_node_1 = {1, 2, 3}
        neighbors_node_2 = {1, 2, 3}
        new_neighbors_node_1, new_neighbors_node_2 = exchange_neighbors(neighbors_node_1=neighbors_node_1,
                                                                        neighbors_node_2=neighbors_node_2,
                                                                        possible_trades_node_1=set(),
                                                                        possible_trades_node_2=set())

        self.assertEqual(new_neighbors_node_1, neighbors_node_1)
        self.assertEqual(new_neighbors_node_2, neighbors_node_2)

    def test_exchange(self):
        """
        One trade is possible,
        then function exchange_neighbors shall return
        either the same neighbors sets as the ones given as input
        or the neighbors sets with one neighbor exchanged
        """
        neighbors_node_1 = {1, 2, 3}
        neighbors_node_2 = {1, 2, 4}
        for _ in range(100):
            new_neighbors_node_1, new_neighbors_node_2 = exchange_neighbors(neighbors_node_1=neighbors_node_1,
                                                                            neighbors_node_2=neighbors_node_2,
                                                                            possible_trades_node_1={3},
                                                                            possible_trades_node_2={4})
            if new_neighbors_node_1 == {1, 2, 3}:
                self.assertEqual(new_neighbors_node_2, {1, 2, 4})
            elif new_neighbors_node_1 == {1, 2, 4}:
                self.assertEqual(new_neighbors_node_2, {1, 2, 3})
            else:
                self.fail(
                    'new_neighbors {} different from expected values (either {{1, 2, 3}} or {{1, 2, 4}})'.format(
                        new_neighbors_node_1
                    )
                )

    def test_keep_degree_while_trading(self):
        """
        Shall always keep the same number of neighbors for each node
        """
        random.seed(0)

        # current neighbors
        neighbors_node_1 = {1, 2, 3}
        neighbors_node_2 = {4, 5, 6}

        for i in range(1000):
            for f in [trade_with_self_loop, trade_without_self_loop]:
                with self.subTest(f=f, i=i):
                    trade = f(index_node_1=1,
                              index_node_2=2,
                              neighbors_node_1=neighbors_node_1,
                              neighbors_node_2=neighbors_node_2)
                    new_neighbors_node_1 = trade[0][1]
                    new_neighbors_node_2 = trade[1][1]
                    self.assertEqual(
                        len(new_neighbors_node_1),
                        len(neighbors_node_1)
                    )
                    self.assertEqual(
                        len(new_neighbors_node_2),
                        len(neighbors_node_2)
                    )

    def test_possible_neighborhoods_with_self_loop(self):
        """
        Running several time a given trade, one expects to see all possible neighborhoods,
        no more no less.

        E.g., with node 1 having {1, 3} as neighbors and
        node 2 having {2, 3} as neighbors,
        the trade shall give {1, 3} or {2, 3} as new neighbors for node 1
        and {1, 3} or {2, 3} as neighbors for node 2
        """
        random.seed(0)

        # current neighbors
        neighbors_node_1 = {1, 3}
        neighbors_node_2 = {2, 3}

        expected_neighborhood = {1: [{1, 3}, {2, 3}], 2: [{2, 3}, {1, 3}]}

        # save the results from the trades
        new_neighborhoods = defaultdict(list)

        for i in range(1000):
            trade = trade_with_self_loop(index_node_1=1,
                                         index_node_2=2,
                                         neighbors_node_1=neighbors_node_1,
                                         neighbors_node_2=neighbors_node_2)
            new_neighbors_node_1 = trade[0][1]
            new_neighbors_node_2 = trade[1][1]
            if new_neighbors_node_1 not in new_neighborhoods[1]:
                new_neighborhoods[1] += [new_neighbors_node_1]
            if new_neighbors_node_2 not in new_neighborhoods[2]:
                new_neighborhoods[2] += [new_neighbors_node_2]

        self.assertCountEqual(new_neighborhoods[1], expected_neighborhood[1])
        self.assertCountEqual(new_neighborhoods[2], expected_neighborhood[2])

    def test_possible_neighborhoods_without_self_loop(self):
        """
        Running several time a given trade, one expects to see all possible neighborhoods,
        no more no less.

        E.g., with node 1 having {1, 3} as neighbors and
        node 2 having {2, 3} as neighbors,
        the trade shall give {1, 3} or {2, 3} as new neighbors for node 1
        and {1, 3} or {2, 3} as neighbors for node 2
        """
        random.seed(0)

        # current neighbors
        neighbors_node_1 = {2, 3}
        neighbors_node_2 = {1, 4}

        expected_neighborhood = {1: [{2, 3}, {2, 4}], 2: [{1, 3}, {1, 4}]}

        # save the results from the trades
        new_neighborhoods = defaultdict(list)

        for i in range(1000):
            trade = trade_without_self_loop(index_node_1=1,
                                            neighbors_node_1=neighbors_node_1,
                                            index_node_2=2,
                                            neighbors_node_2=neighbors_node_2)
            new_neighbors_node_1 = trade[0][1]
            new_neighbors_node_2 = trade[1][1]
            if new_neighbors_node_1 not in new_neighborhoods[1]:
                new_neighborhoods[1] += [new_neighbors_node_1]
            if new_neighbors_node_2 not in new_neighborhoods[2]:
                new_neighborhoods[2] += [new_neighbors_node_2]

        self.assertCountEqual(new_neighborhoods[1], expected_neighborhood[1])
        self.assertCountEqual(new_neighborhoods[2], expected_neighborhood[2])


if __name__ == '__main__':
    unittest.main()
