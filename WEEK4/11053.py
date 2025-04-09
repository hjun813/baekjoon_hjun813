import sys
input = sys.stdin.readline

N = int(input())
Arr = list(map(int, input().split()))


dp = [1] * N
# dp[i] 는 i 까지 최대 길이?

for i in range(N):
    for j in range(i):
        if Arr[j] < Arr[i]:
            dp[i]= max(dp[i], dp[j]+1)
print((max(dp)))
