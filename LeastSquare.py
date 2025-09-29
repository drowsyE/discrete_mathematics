# 가우스 소거법 / 여인수 전개를 통해 얻는 역행렬을 기반으로 최소제곱해를 계산

from utils import transpose, matmul, mat_vec_mul
import Inverse_cofactor
import Inverse_gauss

def least_square(A, b, method = "cofactor"):
    At = transpose(A)
    AtA = matmul(At, A)

    if method == "cofactor":
        AtA_inv = Inverse_cofactor.computeInverse(AtA)
    elif method == "gauss":
        AtA_inv = Inverse_gauss.computeInverse(AtA)
    else:
        raise ValueError("Invalid argument : method must be \"cofactor\" or \"gauss\"")
    
    AtA_inv_At = matmul(AtA_inv, At)
    return mat_vec_mul(AtA_inv_At, b)


if __name__=="__main__":

    n = int(input("연립방정식의 개수를 입력하세요 : "))
    A = []
    for i in range(1,n+1):
        row = list(map(float, input(f"A의 {i}행 : ").split()))
        A.append(row)
    
    print("")
    b = list(map(float, input("b 벡터를 입력하세요. : ").split()))
    
    print(least_square(A, b, method="cofactor"))
    

