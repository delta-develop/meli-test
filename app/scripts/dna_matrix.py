import re
from typing import List


class DNAMatrix:

    MAXIMUM_COINCIDENCES = 2

    def __init__(self, dna_sequences: List) -> None:
        self.dna_sequences = dna_sequences
        self.size = len(dna_sequences)
        self.coincidences = 0

    async def convert_diagonal_to_string(self, i: int, j: int) -> str:
        result = "".join(
            self.dna_sequences[i + k][j + k] for k in range(self.size - i - j)
        )
        return result

    async def pattern_lookup(self, string: str) -> int:
        dna_sequence_patterns: List = ["AAAA", "TTTT", "GGGG", "CCCC"]
        for pattern in dna_sequence_patterns:
            self.coincidences += string.count(pattern)
            if self.coincidences >= DNAMatrix.MAXIMUM_COINCIDENCES:
                return True

        return False

    async def validate_dna_string(self, string: str) -> bool:
        regex = re.compile(r"[^ACGT]")

        if regex.search(string) is not None:
            return False
        return True

    async def diagonal_search(self) -> bool:
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
        for dna_sequence in self.dna_sequences:
            if not await self.validate_dna_string(dna_sequence):
                return None
            if await self.pattern_lookup(dna_sequence):
                return True

        return False

    async def rotate_matrix_90_deg(self) -> None:
        rotated_matrix = []
        last_column = self.size - 1
        first_column = -1
        step = -1

        for j in range(last_column, first_column, step):
            rotated_matrix.append(
                "".join([self.dna_sequences[i][j] for i in range(self.size)])
            )

        self.dna_sequences = rotated_matrix
