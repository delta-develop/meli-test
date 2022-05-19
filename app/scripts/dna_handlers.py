from app.scripts.dna_handler_definition import AbstractDNAHandler
from app.scripts.dna_matrix import DNAMatrix


class RowHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        """Abstraction of the first handler, check row
        by row looking for patterns.

        Args:
            dna_matrix (DNAMatrix): data to analyze.

        Returns:
            bool: True if find two or more patterns, else
            return next handler.
        """
        is_mutant = await dna_matrix.row_search()

        if is_mutant:
            return True
        elif is_mutant is None:
            return None
        else:
            return await super().handle(dna_matrix)


class RightDiagonalHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        """Abstraction of the second handler, check diagonals
        looking for patterns.

        Args:
            dna_matrix (DNAMatrix): data to analyze.

        Returns:
            bool: True if find two or more patterns, else
            return next handler.
        """
        is_mutant = await dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return await super().handle(dna_matrix)


class ColumnHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        """Abstraction of the third handler, rotate the matrix 90º
        and then check row by row looking for patterns.

        Args:
            dna_matrix (DNAMatrix): data to analyze.

        Returns:
            bool: True if find two or more patterns, else
            return next handler.
        """
        await dna_matrix.rotate_matrix_90_deg()
        is_mutant = await dna_matrix.row_search()

        if is_mutant:
            return True
        else:
            return await super().handle(dna_matrix)


class LeftDiagonalHandler(AbstractDNAHandler):
    async def handle(self, dna_matrix: DNAMatrix) -> bool:
        """Abstraction of the last handler, after rotation check
        diagonals, looking for patterns.

        Args:
            dna_matrix (DNAMatrix): data to analyze.

        Returns:
            bool: True if find two or more patterns, else
            return false because is the last chain link.
        """
        is_mutant = await dna_matrix.diagonal_search()

        if is_mutant:
            return True
        else:
            return False
