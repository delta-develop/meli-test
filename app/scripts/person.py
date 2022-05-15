from typing import List
from app.scripts.dna_matrix import DNAMatrix
from app.utils.helpers import timeit
from app.scripts.dna_handler_definition import DNAHandler


class Person:
    def __init__(self, dna_sequences: List[List[str]]) -> None:
        self.dna_matrix = DNAMatrix(dna_sequences)

    @timeit
    def is_mutant(self, dna_handler: DNAHandler) -> None:
        result = dna_handler.handle(self.dna_matrix)
        print(f"is mutant: {result}")
        return result
