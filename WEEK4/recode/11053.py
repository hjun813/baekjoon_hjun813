import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

# dp[i] 는 i 번째 까지 가장 긴 증가하는 수열 수
# 점화식은 
# 
dp[0] = 1
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))