from matrix_diagonals import get_diagonals_in, get_diagonals_re,search_in, search_re
from random import randint
import time
import re

regex = re.compile(r"[A]{4}|[T]{4}|[G]{4}|[C]{4}")


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def get_columns_re(matrix):
    n = len(matrix)
    coincidences = 0

    for i in range(n):
        str_ = "".join(matrix[j][i] for j in range(n))
        coincidences += search_re(str_)

    print(coincidences)

@timeit
def get_columns_in(matrix):
    n = len(matrix)
    coincidences = 0
    for i in range(n):
        str_ = "".join(matrix[j][i] for j in range(n))
        coincidences += search_in(str_)
    
    print(coincidences)
    

@timeit
def rotate_matrix_re(matrix):
    n = len(matrix)
    coincidences = 0
    
    
    for j in range(n-1,-1,-1):  
        str_ = "".join([matrix[i][j] for i in range(n)])
        coincidences += search_re(str_)

    print(coincidences)

@timeit
def rotate_matrix_in(matrix):
    n = len(matrix)
    coincidences = 0
    
    for j in range(n-1,-1,-1):  
        str_ = "".join([matrix[i][j] for i in range(n)])
        coincidences += search_in(str_)

    print(coincidences)

    
@timeit
def generate_matrix(size):
    dna = {1:"A",2:"T",3:"G",4:"C"}   
    dna_matrix = [[dna[randint(1,4)] for i in range(size)] for j in range(size)]
    return dna_matrix



dna_matrix =   ["XATGCGA",
                "CXAGTGC",
                "TTXATGT",
                "AGAXAGG",
                "CCCCXTA",
                "TCACTXG",
                "XXXXXXX"]


dna_matrix = generate_matrix(1000)


# print(" \n".join(" ".join(row) for row in dna_matrix))
# print("\n")

get_diagonals_re(dna_matrix)
get_diagonals_in(dna_matrix)

get_columns_re(dna_matrix)
get_columns_in(dna_matrix)

rotate_matrix_re(dna_matrix)
rotate_matrix_in(dna_matrix)


# get_columns(dna_matrix)
# get_right_diagonals(dna_matrix)
# print("\n")
# rotated_matrix = rotate_matrix(dna_matrix)
# print(" \n".join(" ".join(row) for row in rotated_matrix))
# print("\n")
# get_right_diagonals(rotated_matrix)
