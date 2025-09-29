# Implementation of calculating inverse matrix by cofactor expansion
# A^-1 = adj(A)/|A|

from utils import computeDet, transpose, getMinor

def computeInverse(mat):
    det = computeDet(mat)

    if (det == 0):
        raise ValueError("Matrix is singular, no inverse exists")

    # Calculate adjoint matrix
    n = len(mat)
    adjMat = []
    for i in range(n):
        cofactors = []
        for j in range(n):
            cofactor = (-1)**(i+j) * computeDet(getMinor(mat, i ,j))
            cofactors.append(cofactor)
        adjMat.append(cofactors)

    adjMat = transpose(adjMat)
    # divide determinant
    for i in range(n):
        for j in range(n):
            adjMat[i][j] /= det
            
    return adjMat


if __name__ == "__main__":
    
    matrix = [
        [1,2,3],
        [0,1,4],
        [5,6,0]
    ]
    for row in computeInverse(matrix):
        print(row)
        
