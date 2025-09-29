from LeastSquare import * 
import random

if __name__ == "__main__":

    # 테스트용 데이터 (4차 다항식)
    x = [-2.0, -1.5556, -1.1111, -0.6667, -0.2222, 0.2222, 0.6667, 1.1111, 1.5556, 2.0]

    # 행렬 A : [1, x, x^2, x^3, x^4]
    A = [[1, xi, xi**2, xi**3, xi**4] for xi in x]

    # 원래 y 값
    y_true = [1 + 2*xi - 0.5*xi**2 + xi**3 - 0.2*xi**4 for xi in x]

    # 평균 = 0, 분산 = 0.5인 가우시안 노이즈 첨기
    b = [yi + random.gauss(0, 0.5) for yi in y_true]

    coef = least_square(A, b, method="cofactor")
    
    print()
    print("최소제곱 해 (계수) :", coef)
    print()

    # 실제 값 계산, x=3
    x = 3
    gt = 1 + 2*x - 0.5*x**2 + x**3 - 0.2*x**4
    # 예측한 계수들로 계산
    pred = coef[0] + coef[1]*x + coef[2]*x**2 + coef[3]*x**3 + coef[4]*x**4
    print(f"x = 3에서의 오차 : {gt - pred}")
    print()