# 재귀함수로 피보나치 구현 -> 중복된 계산이 많다
import sys
input = sys.stdin.readline
n = int(input())
# dp = [0] * (n+1)

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print(fibo(n+1))


######################
# 작은 값부터 for 문 반복을 통해 구하는 bottom up 테뷸레이션
import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

def fibo(n):
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibo(n))
print(dp)

##############################
# 메모지 네이션 top-down 
import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

def fibo(n):
    if n == 0:
        return dp[0]
    if n == 1: 
        return dp[1]
    
    dp[n] = fibo(n-1) + dp[n-2]

    return dp[n]

print(fibo(n))
print(dp)
####################################
# 메모지 네이션 top-down
import sys
input = sys.stdin.readline
n = int(input())
dp = [-1] * (n+1)

def fibo(n):
    if dp[n] == -1:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

dp[0] = 0
dp[1] = 1
print(fibo(n))
