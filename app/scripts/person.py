from app.scripts.dna_matrix import DNAMatrix
from app.scripts.dna_handler_definition import DNAHandler
from typing import Any, List


class Person:
    def __init__(self, dna_sequences: List[Any]) -> None:
        self.dna_matrix = DNAMatrix(dna_sequences)

    def is_mutant(self, dna_handler: DNAHandler) -> bool:
        result = dna_handler.handle(self.dna_matrix)
        return result
