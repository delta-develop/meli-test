from utils import *
from matrix_operations import *


@timeit
def is_mutant():
    dna_matrix = generate_matrix(size=5000)
    # print_matrix(dna_matrix)
    # search_in_rows(dna_matrix)
    search_in_diagonals(dna_matrix)
    # dna_matrix = rotate_matrix_90_deg(dna_matrix)
    # search_in_diagonals(dna_matrix)
    # search_in_rows(dna_matrix)


is_mutant()
