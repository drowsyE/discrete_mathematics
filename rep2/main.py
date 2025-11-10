from check_relation import *
from compute_closure import *
from utils import *

def main(rand_gen=False) -> None:

    N = 5
    # 1. 관계 행렬 입력 기능
    if rand_gen:
        matrix = generate_relation_matrix(N, threshold=0.65)
        print("\n관계 행렬 :")
        print_mat(matrix)
    else:
        print(f"\n{N} x {N} 행렬을 입력하시오.")
        matrix = [list(map(int, input(f"{i+1}행 : ").split())) for i in range(N)]
    
    # 2. 동치 관계 판별 기능
    is_equi, is_refl, is_sym, is_trans = check_equi(matrix)
    print(f"\n동치 관계인가? : {is_equi}")
    print(f"반사 관계인가? : {is_refl}")
    print(f"대칭 관계인가? : {is_sym}")
    print(f"추이 관계인가? : {is_trans}\n")

    # 3. 동치 관계인 경우 동치류를 판별하는 기능
    if is_equi:
        print_equi_class(matrix)

    # 4. 폐포 구현 기능
    if not is_equi:
        print("폐포 변환 전 :")
        print_mat(matrix)
        print()

    if not is_refl:
        refl_closure = to_refl_closure(matrix)
        print("반사 폐포 :")
        print_mat(refl_closure)
        print()

        if check_equi(refl_closure)[0]:
            print("반사 폐포는 동치 관계입니다.\n")
            print_equi_class(refl_closure)
            print()
        else:
            print("반사 폐포는 동치 관계가 아닙니다.\n")
    
    if not is_sym:
        sym_closure = to_sym_closure(matrix)
        print("대칭 폐포 :")
        print_mat(sym_closure)
        print()

        if check_equi(sym_closure)[0]:
            print("대칭 폐포는 동치 관계입니다.\n")
            print_equi_class(sym_closure)
            print()
        else:
            print("대칭 폐포는 동치 관계가 아닙니다.\n")

    if not is_trans:
        trans_closure = to_trans_closure(matrix)
        print("추이 폐포 : ")
        print_mat(trans_closure)
        print()

        if check_equi(trans_closure)[0]:
            print("추이 폐포는 동치 관계입니다.\n")
            print_equi_class(trans_closure)
            print()
        else:
            print("추이 폐포는 동치 관계가 아닙니다.\n")
    
    print()
main(rand_gen=False)