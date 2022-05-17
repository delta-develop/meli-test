import time
from random import randint
from typing import List
from app.scripts.dna_handlers import (
    RowHandler,
    RightDiagonalHandler,
    LeftDiagonalHandler,
    ColumnHandler,
)


# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         print("%r  %2.2f us" % (method.__name__, (te - ts) * 1000000))
#         return result

#     return timed


# def generate_matrix(size: int) -> List[List[str]]:
#     dna = {1: "A", 2: "T", 3: "G", 4: "C"}
#     dna_matrix = [[dna[randint(1, 4)] for i in range(size)] for j in range(size)]
#     return dna_matrix


# def print_matrix(matrix: List[List[str]]) -> None:
#     for row in matrix:
#         dna_sequence = " ".join(row)
#         print(dna_sequence)


def configure_handlers():
    row = RowHandler()
    right_diagonal = RightDiagonalHandler()
    left_diagonal = LeftDiagonalHandler()
    column = ColumnHandler()

    row.set_next(right_diagonal).set_next(column).set_next(left_diagonal)

    return row
