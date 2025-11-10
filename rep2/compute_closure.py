def to_refl_closure(mat) -> list[list[int]]:
    refl_closure = [row[:] for row in mat]
    for i in range(len(refl_closure)):
        refl_closure[i][i] = 1
    return refl_closure

def to_sym_closure(mat) -> list[list[int]]:
    sym_closure = [row[:] for row in mat]
    size = len(mat)
    for i in range(size):
        for j in range(size):
            sym_closure[i][j] = mat[i][j] | mat[j][i]
    return sym_closure

# calculate transitive closure via warshall algorithm
def to_trans_closure(mat) -> list[list[int]]: 
    size = len(mat)
    trans_closure = [row[:] for row in mat]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if not trans_closure[i][j] and trans_closure[i][k] and trans_closure[k][j]:
                    trans_closure[i][j] = 1
    return trans_closure