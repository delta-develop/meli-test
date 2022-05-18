from app.scripts.dna_matrix import DNAMatrix
from app.scripts.dna_handler_definition import DNAHandler
from typing import Any, List


class Person:
    def __init__(self, dna_sequences: List[Any]):
        self.dna_matrix = DNAMatrix(dna_sequences)

    async def is_mutant(self, dna_handler: DNAHandler):
        result = dna_handler.handle(self.dna_matrix)
        return result
