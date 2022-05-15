from utils import diagonal_to_string, pattern_lookup, timeit


@timeit
def search_in_diagonals(dna_matrix):
    matrix_size = len(dna_matrix)
    group_size = 4
    coincidences = 0
    matrix_border = matrix_size - group_size + 1

    for j in range(matrix_border):
        dna_sequence = diagonal_to_string(
            matrix=dna_matrix, matrix_size=matrix_size, i=0, j=j
        )
        coincidences += pattern_lookup(dna_sequence)

    for i in range(1, matrix_border):
        dna_sequence = diagonal_to_string(
            matrix=dna_matrix, matrix_size=matrix_size, i=i, j=0
        )
        coincidences += pattern_lookup(dna_sequence)

    print(f"Diagonals: {coincidences}")


@timeit
def rotate_matrix_90_deg(matrix):
    matrix_size = len(matrix)
    rotated_matrix = []
    last_column = matrix_size - 1
    first_column = -1
    step = -1

    for j in range(last_column, first_column, step):
        rotated_matrix.append([matrix[i][j] for i in range(matrix_size)])

    return rotated_matrix


@timeit
def search_in_rows(matrix):
    coincidences = 0

    for row in matrix:
        adn_sequence = "".join(row)
        coincidences += pattern_lookup(adn_sequence)

    print(f"Rows: {coincidences}")
