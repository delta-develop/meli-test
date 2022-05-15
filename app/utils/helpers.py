import time
from random import randint
from typing import List


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("%r  %2.2f us" % (method.__name__, (te - ts) * 1000000))
        return result

    return timed


@timeit
def generate_matrix(size: int) -> List[List[str]]:
    dna = {1: "A", 2: "T", 3: "G", 4: "C"}
    dna_matrix = [[dna[randint(1, 4)] for i in range(size)] for j in range(size)]
    return dna_matrix


def print_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        dna_sequence = " ".join(row)
        print(dna_sequence)
