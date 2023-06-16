import math

def find_fraction(x):
    n = math.ceil((-1 + math.sqrt(1 + 8 * x)) / 2)  # 라인의 번호 구하기
    count = n * (n - 1) // 2  # 현재 라인 직전까지의 분수 개수

    if n % 2 == 0:  # 짝수 번째 라인
        numerator = x - count
        denominator = n - numerator + 1
    else:  # 홀수 번째 라인
        denominator = x - count
        numerator = n - denominator + 1

    return f"{numerator}/{denominator}"

# 입력 받기
T = int(input())

# 결과 출력
print(find_fraction(T))
