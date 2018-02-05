"""
Here is an example of an undirected graph with 8 nodes
and the following degree distribution:
2 nodes with degree k = 1
4 nodes with degree k = 2
2 nodes with degree k = 3
"""
a_digraph_with_loops = [
    {
        1: {2},
        2: {3},
        3: {4},
        4: {1},
    }, {
        1: {1},
        2: {3},
        3: {4},
        4: {2},
    }, {
        1: {1},
        2: {2},
        3: {4},
        4: {3},
    }, {
        1: {1},
        2: {2},
        3: {3},
        4: {4},
    }, {
        1: {2},
        2: {1},
        3: {4},
        4: {3},
    },
]
