import cProfile
from multiprocessing import Pool

def f(x):
    return x*x

def square(values):
    return [f(x) for x in values]

def square_multiprocessing(nb_workers, values):
    with Pool(nb_workers) as p:
        return p.map(f, values)


if __name__ == '__main__':
    values = [x for x in range(10000)]
    nb_workers = 5
    cProfile.run('square(values)')
    cProfile.run('square_multiprocessing(nb_workers,values)')
