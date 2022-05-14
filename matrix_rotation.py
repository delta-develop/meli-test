import numpy as np
from scipy.ndimage import rotate

def adn_to_matrix(adn):
    matrix = []
    n = len(matrix)
    for row in range(n):
        print([matrix[j][row] for j in range(n)])

def rotate_matrix():
    x = np.array([[1,2,3],[4,1,2],[3,4,1]])
    print(x)
    x = rotate(x,angle=45,reshape=True)
    print(x)
    x = np.arange(25).reshape(5, -1)
    x = rotate(x, angle=45) 
    print(x)


rotate_matrix()