from app.scripts.dna_handler_definition import AbstractDNAHandler
from app.scripts.dna_matrix import DNAMatrix


class RowHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        is_mutant = await dna_matrix.row_search()

        if is_mutant:
            return True
        elif is_mutant is None:
            return None
        else:
            return await super().handle(dna_matrix)


class RightDiagonalHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        is_mutant = await dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return await super().handle(dna_matrix)


class LeftDiagonalHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        is_mutant = await dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return False


class ColumnHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        await dna_matrix.rotate_matrix_90_deg()
        is_mutant = await dna_matrix.row_search()

        if is_mutant:
            return True
        else:
            return await super().handle(dna_matrix)
