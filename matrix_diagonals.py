

import re
import time

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


def get_right_diagonals_1(dna_matrix):
    print(" \n".join(" ".join(row) for row in dna_matrix))
    print("\n")
    n = len(dna_matrix)
    limit = 4
    
    for i in range(n,0,-1):
        if i + limit < n:
            for j in range(n):
                if j + limit < n:
                    print(f"i: {i}, j: {j}")
                    str_ = ""
                    for k in range(n-1):
                        str_ += " ".join(dna_matrix[i+k][j+k])
                        print(f"i: {i+k}, j: {j+k}")
                    print(str_)
                else:
                    continue
        else:
            continue


def get_right_diagonals_2(dna_matrix):
    print(" \n".join(" ".join(row) for row in dna_matrix))
    print("\n")
    n = len(dna_matrix)
    limit = 4
    
    for i in range(n):
        if i + limit < n:
            for j in range(n):
               if j + limit < n: 
                    str_ = ""
                    for k in range(n-i-j):
                        str_ += " ".join(dna_matrix[i+k][j+k])
                    print(str_)

@timeit           
def get_diagonals_re(dna_matrix):
    n = len(dna_matrix)
    group_size = 4
    coincidences = 0

    i = 0
    for j in range(n-group_size+1):
        str_ = diagonal_to_string(dna_matrix,n,i,j)
        coincidences += search_re(str_)

    j = 0
    for i in range(1,n-group_size+1):
        str_ = diagonal_to_string(dna_matrix,n,i,j)
        coincidences += search_re(str_)
    
    print(coincidences)

@timeit
def get_diagonals_in(dna_matrix):
    n = len(dna_matrix)
    group_size = 4
    coincidences = 0

    i = 0
    for j in range(n-group_size+1):
        str_ = diagonal_to_string(dna_matrix,n,i,j)
        coincidences += search_in(str_)

    j = 0
    for i in range(1,n-group_size+1):
        str_ = diagonal_to_string(dna_matrix,n,i,j)
        coincidences += search_in(str_)
    
    print(coincidences)

def search_re(string):
    coincidences = len(regex.findall(string))
    return coincidences

def search_in(string):
    coincidences = 0
    for pattern in ["AAAA","TTTT","GGGG","CCCC"]:
        coincidences += string.count(pattern)
    
    return coincidences


def diagonal_to_string(matrix,n,i,j):
    return "".join(matrix[i+k][j+k] for k in range(n-i-j))     

# dna_matrix =   ["XATGCGA",
#                 "CXAGTGC",
#                 "TTXATGT",
#                 "AGAXAGG",
#                 "CCCCXTA",
#                 "TCACTXG",
#                 "XXXXXXX"]

# print(" \n".join(" ".join(row) for row in dna_matrix))
# print("\n")
# get_right_diagonals(dna_matrix)