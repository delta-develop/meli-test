

from random import randint


def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j])

n = 100
dna = {1:"A",2:"B",3:"C",4:"D"}    
matrix = [[dna[randint(1,4)] for i in range(n)] for j in range(n)]
print_matrix(matrix)