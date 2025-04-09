import sys
input = sys.stdin.readline

N = int(input())
col = (N//3)+2
row = (N//5)+2
dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
kilo = [3,5]

def fun1():
    global dp

    for num in range(1, N+1):
        for i in range(num+1):
            j = num - i
            dp[j][i] = 3 * j + 5 * i
            if dp[j][i] == N :
                return i+j
            if i == 0:
                if dp[j][i] > N:
                    return -1
if N == 3:
    print(1)
elif N < 5:
    print(-1)
else:                
    print(fun1())
# print(dp)