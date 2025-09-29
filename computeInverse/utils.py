def matmul(mat1, mat2):
    r1, c1 = len(mat1), len(mat1[0])
    r2, c2 = len(mat2), len(mat2[0])

    if (c1 != r2):
        raise ValueError("Cannot multiply between two matrices")

    mat3 = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3

def mat_vec_mul(mat, vec): # 열벡터 관행을 따름
    mat_r, mat_c = len(mat), len(mat[0])
    vec_r = len(vec)
    if mat_c != vec_r:
        raise ValueError("Cannot multiply between matrix and vector")
    
    vec_out = [0] * mat_r
    for i in range(mat_r):
        for j in range(mat_c):
            vec_out[i] += mat[i][j] * vec[j]
    return vec_out

def computeDet(mat):
    r, c = len(mat), len(mat[0])
    if (r != c):
        raise ValueError("Invaild input. Input must be square matrix")

    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    
    det = 0
    for col in range(c): # decompose minor matrix recursively until it becomes 2x2
        det += (-1)**col * mat[0][col] * computeDet(getMinor(mat, 0, col))
    return det

# For cofactor expansion

def getMinor(mat, r, c):
    return [row[:c] + row[c+1:] for row in mat[:r] + mat[r+1:]]

def transpose(mat):
    r, c = len(mat), len(mat[0])
    return [[mat[j][i] for j in range(r)] for i in range(c)]

# For Gauss-Jordan elimination (Elementary row operations)

def mutiply_row(row, k):
    return [x * k for x in row]

def add_row_to_other(dst_row, src_row, k=1.0):
    return [d + k * s for d, s in zip(dst_row, src_row)]
