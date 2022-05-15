from utils import diagonal_to_string, pattern_lookup, timeit


@timeit
def search_in_diagonals(dna_matrix):
    n = len(dna_matrix)
    group_size = 4
    coincidences = 0

    for j in range(n - group_size + 1):
        str_ = diagonal_to_string(matrix=dna_matrix, n=n, i=0, j=j)
        coincidences += pattern_lookup(str_)

    for i in range(1, n - group_size + 1):
        str_ = diagonal_to_string(matrix=dna_matrix, n=n, i=i, j=0)
        coincidences += pattern_lookup(str_)

    print(f"dual for: {coincidences}")


@timeit
def rotate_matrix_90_deg(matrix):
    n = len(matrix)
    rotated_matrix = []

    for j in range(n - 1, -1, -1):
        rotated_matrix.append([matrix[i][j] for i in range(n)])

    return rotated_matrix


@timeit
def search_in_rows(matrix):
    coincidences = 0

    for row in matrix:
        adn_sequence = "".join(row)
        coincidences += pattern_lookup(adn_sequence)

    print(f"Rows: {coincidences}")
