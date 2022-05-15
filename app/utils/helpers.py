import time
from random import randint
from typing import List


def pattern_lookup(string: str) -> int:
    coincidences: int = 0
    dna_sequence_patterns: List = ["AAAA", "TTTT", "GGGG", "CCCC"]
    for pattern in dna_sequence_patterns:
        coincidences += string.count(pattern)

    return coincidences


def diagonal_to_string(
    matrix: List[List[str]], matrix_size: int, i: int, j: int
) -> str:
    return "".join(matrix[i + k][j + k] for k in range(matrix_size - i - j))


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
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
