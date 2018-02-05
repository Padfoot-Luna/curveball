# Python Implementation of the Curveball Algorithm

This algorithm is used to generate uniformly at random graphs (nodes + links) with a fixed degree distribution

## Implementations

As defined by C. J. Carstens, A. Berger, and G. Strona in [Curveball: a new generation of sampling
algorithms for graphs with fixed degree sequence](https://arxiv.org/abs/1609.05137)


## Structure of the package

 - curveball: contains the different implementations of the curveball algorithm
 - experiments: contains scripts to run experiments (generating several random graphs, saving them, computing cooccurence on theses random graphs...), also used for profiling
 - fsdm: (deprecated) other Fixed Degree Sequence Model algorithms
 - tests: unit test and statistical test
 - utilities: useful functions like loading, saving graphs, computing isomorphisms (networkx)...
