import sys

A, B, C = map(int, sys.stdin.readline().split())

# x = A % C

def restFunction(a, b, c):
    result = 1
    a = a % c  # a를 미리 c로 나눈 나머지를 구해 최적화
    
    while b > 0:
        if b % 2 == 1:  # 지수가 홀수일 때 보정
            result = (result * a) % c # 홀수면은 B-1한다음에 1/2할라고

        # A^B 를 (A^2)^(1/2 B)로 계산 할라고
        a = (a * a) % c  # 제곱 연산
        b //= 2  # 지수를 반으로 줄이기

    return result


print(restFunction(A, B, C))

# print(pow(x, B, C))

# x = A % C 일때
# A**B % C 와 x**B % C가 같다.