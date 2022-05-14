def get_rows(matrix):
    n = len(matrix)

    for row in matrix:
        print(row)
    

def get_columns(matrix):
    n = len(matrix)
    for row in range(n):
        print([matrix[j][row] for j in range(n)]) # Esto es una solución cuadrática


def get_right_diagonal(matrix):
    ...

def get_left_diagonal(matrix):
    ...


matrix = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

get_rows(matrix)
get_columns(matrix)