import Inverse_cofactor
import Inverse_gauss

# 코드 중간중간의 print()문은 깔끔한 출력을 위한 것입니다.
def run():

    print()
    n = int(input("정방행렬의 차수를 입력하세요 : "))
    matrix = []
    for i in range(1,n+1):
        row = list(map(float, input(f"{i}행 : ").split()))
        matrix.append(row)
    
    print()
    print("행렬식(여인수 전개)으로 구한 역행렬 : ")
    inv_cof = Inverse_cofactor.computeInverse(matrix)
    for row in inv_cof:
        print(row)

    print()
    print("가우스 소거법으로 구한 역행렬 : ")
    inv_gauss = Inverse_gauss.computeInverse(matrix)
    for row in inv_gauss:
        print(row)
    
    print()
    is_same = True
    for i in range(n):
        for j in range(n):
            if abs(inv_cof[i][j] - inv_gauss[i][j]) > 1e-7:
                is_same = False
                break
        if (not is_same):
            break
    if is_same:
        print("두 결과가 같습니다.")
    else:
        print("두 결과가 같지 않습니다.")
    print()


run()