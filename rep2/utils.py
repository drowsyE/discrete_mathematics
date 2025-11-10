def product(mat1, mat2) -> list[list[int]]:
    size = len(mat1)
    mat3 = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                mat3[i][j] |= (mat1[i][k] & mat2[k][j])
    return mat3

def transpose(mat) -> list[int]: 
    mat2 = []
    size = len(mat)
    for i in range(size):
        row = [mat[j][i] for j in range(size)]
        mat2.append(row)
    return mat2

def print_mat(mat) -> None:
    for row in mat:
        for e in row:
            print(e, end=" ")
        print()

def print_equi_class(mat) -> None:
    print("동치류 :")
    size = len(mat)
    for i in range(size):
        print(f"[{i+1}] = ", end = "{")
        for j in range(size):
            if mat[i][j]:
                print(j+1, end=", ")
        print("\b\b}")

def generate_relation_matrix(N, threshold = 0.5):
    import random
    return [[int(random.random() > threshold) for _ in range(N)]for _ in range(N)]

if __name__=="__main__":
    print(generate_relation_matrix(5))