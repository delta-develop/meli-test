from app.scripts.dna_handler_definition import AbstractDNAHandler
from typing import Any, List


class RowHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: List) -> bool:
        is_mutant = dna_matrix.row_search()

        if is_mutant:
            return True
        else:
            return super().handle(dna_matrix)


class RightDiagonalHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: List) -> bool:
        is_mutant = dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return super().handle(dna_matrix)


class LeftDiagonalHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: List) -> bool:
        is_mutant = dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return False


class ColumnHandler(AbstractDNAHandler):
    def handle(self, dna_matrix: List) -> bool:
        dna_matrix.rotate_matrix_90_deg()
        is_mutant = dna_matrix.row_search()

        if is_mutant:
            return True
        else:
            return super().handle(dna_matrix)
