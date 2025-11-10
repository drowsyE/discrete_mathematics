from utils import transpose, product

def check_refl(mat) -> bool:
    return sum(mat[i][i] for i in range(len(mat))) == len(mat)

def check_sym(mat) -> bool:
    return mat == transpose(mat)

def check_trans(mat) -> bool:
    size = len(mat)
    power = [row[:] for row in mat]
    combined = [row[:] for row in mat]

    for _ in range(1, size):
        power = product(power, mat)
        for i in range(size):
            for j in range(size):
                combined[i][j] |= power[i][j]
    return mat == combined

def check_equi(mat) -> tuple[bool, bool, bool, bool]:
    b1 = check_refl(mat)
    b2 = check_sym(mat)
    b3 = check_trans(mat)
    return (b1 and b2 and b3, b1, b2, b3)