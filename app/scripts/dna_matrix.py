from typing import List
from app.utils.helpers import timeit


class DNAMatrix:
    def __init__(self, dna_sequences: List) -> None:
        self.dna_sequences = dna_sequences
        self.size = len(dna_sequences)

    def __print_dna_matrix(self) -> None:
        for row in self.dna_sequences:
            dna_sequence = " ".join(row)
            print(dna_sequence)

    def __convert_diagonal_to_string(self, i: int, j: int) -> str:
        result = "".join(
            self.dna_sequences[i + k][j + k] for k in range(self.size - i - j)
        )
        return result

    @staticmethod
    def pattern_lookup(string) -> int:
        dna_sequence_patterns = ["AAAA", "TTTT", "GGGG", "CCCC"]
        coincidences = 0
        for pattern in dna_sequence_patterns:
            coincidences += string.count(pattern)

        return coincidences

    @timeit
    def diagonal_search(self) -> None:
        group_size = 4
        coincidences = 0
        matrix_border = self.size - group_size + 1

        for j in range(matrix_border):
            dna_sequence = self.__convert_diagonal_to_string(i=0, j=j)
            coincidences += DNAMatrix.pattern_lookup(dna_sequence)

        for i in range(1, matrix_border):
            dna_sequence = self.__convert_diagonal_to_string(i=i, j=0)
            coincidences += DNAMatrix.pattern_lookup(dna_sequence)

        print(f"Diagonals: {coincidences}")

    @timeit
    def row_search(self) -> None:
        coincidences = 0

        for row in self.dna_sequences:
            dna_sequence = "".join(row)
            coincidences += DNAMatrix.pattern_lookup(dna_sequence)

        print(f"Rows: {coincidences}")

    @timeit
    def rotate_matrix_90_deg(self) -> None:
        rotated_matrix = []
        last_column = self.size - 1
        first_column = -1
        step = -1

        for j in range(last_column, first_column, step):
            rotated_matrix.append([self.dna_sequences[i][j] for i in range(self.size)])

        self.dna_sequences = rotated_matrix
