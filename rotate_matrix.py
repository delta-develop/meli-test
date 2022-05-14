from matrix_diagonals import get_right_diagonals
from random import randint
import time

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
def get_columns(matrix):
    n = len(matrix)
    for i in range(n):
        str_ = "".join(matrix[j][i] for j in range(n))
        print(str_)
    
    print("\n")

@timeit
def rotate_matrix(matrix):
    n = len(matrix)
    rotated = []
    
    for j in range(n-1,-1,-1):  
        rotated.append("".join([matrix[i][j] for i in range(n)]))  

    return rotated





dna_matrix =   ["XATGCGA",
                "CXAGTGC",
                "TTXATGT",
                "AGAXAGG",
                "CCCCXTA",
                "TCACTXG",
                "XXXXXXX"]


dna = {1:"A",2:"T",3:"G",4:"C"}   
n = 100 
dna_matrix = [[dna[randint(1,4)] for i in range(n)] for j in range(n)]

print(" \n".join(" ".join(row) for row in dna_matrix))
print("\n")
# get_columns(dna_matrix)
get_right_diagonals(dna_matrix)
print("\n")
rotated_matrix = rotate_matrix(dna_matrix)
print(" \n".join(" ".join(row) for row in rotated_matrix))
print("\n")
get_right_diagonals(rotated_matrix)
