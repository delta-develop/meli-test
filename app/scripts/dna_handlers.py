from app.scripts.dna_handler_definition import AbstractDNAHandler
from typing import Any, List
from app.scripts.dna_matrix import DNAMatrix


class RowHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: DNAMatrix) -> bool:
        is_mutant = dna_matrix.row_search()

        if is_mutant:
            return True
        else:
            return super().handle(dna_matrix)


class RightDiagonalHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: DNAMatrix) -> bool:
        is_mutant = dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return super().handle(dna_matrix)


class LeftDiagonalHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: DNAMatrix) -> bool:
        is_mutant = dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return False


class ColumnHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: DNAMatrix) -> bool:
        dna_matrix.rotate_matrix_90_deg()
        is_mutant = dna_matrix.row_search()

        if is_mutant:
            return True
        else:
            return super().handle(dna_matrix)
