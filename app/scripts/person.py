from typing import List
from app.scripts.dna_matrix import DNAMatrix
from app.utils.helpers import timeit


class Person:
    def __init__(self, dna_sequences: List[List[str]]) -> None:
        self.dna_matrix = DNAMatrix(dna_sequences)

    @timeit
    def is_mutant(self):
        self.dna_matrix.row_search()
        self.dna_matrix.diagonal_search()
        self.dna_matrix.rotate_matrix_90_deg()
        self.dna_matrix.diagonal_search()
        self.dna_matrix.row_search()
