import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * (n+1) # dp[i]는 i 번째 피보나치 수
dp[0] = 0
dp[1] = 1

def fibo(n):
    if n == 1:
        return dp[1]
    elif n == 0:
        return dp[0]
    else:
        if dp[n] != 0:
            return dp[n]
        else :
            dp[n] = fibo(n-1) + fibo(n-2)
            return dp[n]
    
print(fibo(n))