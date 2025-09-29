# Implementation of calculating inverse matrix by Gauss-Jordan Elimination

from utils import mutiply_row, add_row_to_other

# 11번 슬라이드의 결과를 출력하기 위해 만든 함수입니다.
# 가우스-조던 소거법의 과정을 보고 싶으시다면 computeInverse 함수 내부의 print_mat 함수를
# 모두 주석 해제하시면 됩니다.
def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()
    print()

def computeInverse(mat):
    r, c = len(mat), len(mat[0])

    if (r != c):
        raise ValueError("Number of rows and columns should be same")

    # make augmented matrix
    aug_mat = []
    for i in range(r):
        row = [0.0] * (c*2)
        for j in range(c):
            row[j] = mat[i][j] # copy matrix
        row[j+1+i] = 1.0 # copy identity matrix
        aug_mat.append(row)

    # print_mat(aug_mat)
    # forward elimination
    for i in range(r):
        if (aug_mat[i][i] == 0):
            # swap between two rows if pivot == 0
            for k in range(i+1, r):
                if aug_mat[k][i] != 0:
                    aug_mat[i], aug_mat[k] = aug_mat[k], aug_mat[i]
                    # print_mat(aug_mat)
                    break
            else:
                raise ValueError("Matrix is singular, no inverse exists")
            
        # make leading-1
        aug_mat[i] = mutiply_row(aug_mat[i], 1/aug_mat[i][i])
        # print_mat(aug_mat)
        
        # eliminate below
        for j in range(i+1,r):
            if aug_mat[j][i] != 0:
                aug_mat[j] = add_row_to_other(aug_mat[j], aug_mat[i], k = (-1) * aug_mat[j][i])
            # print_mat(aug_mat)
    
    # backward elimination
    for i in range(r-1,0,-1):
        for j in range(i-1,-1,-1):
            if aug_mat[j][i] != 0:
                aug_mat[j] = add_row_to_other(aug_mat[j], aug_mat[i], k = (-1) * aug_mat[j][i])
        # print_mat(aug_mat)

    inv = [row[c:] for row in aug_mat]
    return inv

if __name__ == "__main__":
    
    matrix = [
        [1.0,2.0,3.0],
        [0.0,1.0,4.0],
        [5.0,6.0,0.0]
    ]
    for row in computeInverse(matrix):
        print(row)
        

