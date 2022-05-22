import os
import re
from typing import List


class DNAMatrix:
    """This class define all the behaviour related to search patterns in the given
    matrices.
    """

    MINIMUM_COINCIDENCES = os.getenv("MINIMUM_COINCIDENCES", 3)

    def __init__(self, dna_sequences: List) -> None:
        """Each matrix is initialized with the dna matrix data, the size of that
        sequences and the coincidences found in zero.

        Args:
            dna_sequences (List): dna matrix data.
        """
        self.dna_sequences = dna_sequences
        self.size = len(dna_sequences)
        self.coincidences = 0

    async def convert_diagonal_to_string(self, i: int, j: int) -> str:
        """Receive the index of the starting point and iterate, converting diagonals
        into strings to be analyzed.

            i (int): index of row.
            j (int): index of column.

        Returns:
            str: diagonal expresed as string.
        """
        result = "".join(
            self.dna_sequences[i + k][j + k] for k in range(self.size - i - j)
        )
        return result

    async def pattern_lookup(self, string: str) -> bool:
        """Check in a string if it have anny of the looked patterns.
        Note: After a performance test, I decided to use "in" operator
        instead a regex, because "in" ran up to 33% faster, tested with
        strings from 6 elements to 10,000.

        Args:
            string (str): DNA string to analyze.

        Returns:
            bool: True if the coincidences for given matrix reach the goal
            False if not.
        """
        dna_sequence_patterns: List = ["AAAA", "TTTT", "GGGG", "CCCC"]
        for pattern in dna_sequence_patterns:
            self.coincidences += string.count(pattern)
            if self.coincidences >= DNAMatrix.MINIMUM_COINCIDENCES:
                return True

        return False

    async def validate_dna_string(self, string: str) -> bool:
        regex = re.compile(r"[^ACGT]")

        if regex.search(string) is not None:
            return False
        return True

    async def diagonal_search(self) -> bool:
        """This method search patterns in the diagonals of the matrix, iterating
        first at the superior triangle and last the inferior one, only where the
        length of the diagonal is at least the group size we are looking for
        i.e. if we have a 6x6 matrix, it will search first on the A positions,
        then the B positions and the X elements will not be accesed.

                                    A A A X X X
                                    B A A A X X
                                    B B A A A X
                                    X B B A A A
                                    X X B B A A
                                    X X X B B A

        Returns:
            bool: return True if the coincidences of all matrix reach the pattern
            goal (in this case 2) and false if not.
        """
        group_size = 4
        matrix_border = self.size - group_size + 1

        for j in range(matrix_border):
            dna_sequence = await self.convert_diagonal_to_string(i=0, j=j)
            if await self.pattern_lookup(dna_sequence):
                return True

        for i in range(1, matrix_border):
            dna_sequence = await self.convert_diagonal_to_string(i=i, j=0)
            if await self.pattern_lookup(dna_sequence):
                return True

        return False

    async def row_search(self) -> bool:
        """This method iterate over the rows and look for the pattern.

        Returns:
            bool: True if the coincidences for given matrix reach the goal
            False if not.
        """
        for dna_sequence in self.dna_sequences:
            if not await self.validate_dna_string(dna_sequence):
                return None
            if await self.pattern_lookup(dna_sequence):
                return True

        return False

    async def rotate_matrix_90_deg(self) -> None:
        """To check the columns and right diagonal elements, this method rotate
        the matrix 90ª anticlockwise and save the result into the object.
        """
        rotated_matrix = []
        last_column = self.size - 1
        first_column = -1
        step = -1

        for j in range(last_column, first_column, step):
            rotated_matrix.append(
                "".join([self.dna_sequences[i][j] for i in range(self.size)])
            )

        self.dna_sequences = rotated_matrix
