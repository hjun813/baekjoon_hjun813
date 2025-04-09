import sys
input = sys.stdin.readline

s1 = list(map(str, input().strip()))
s2 = list(map(str, input().strip()))

# print(s1)
# print(s2)

dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            
# for i in range(len(s1)+1):
#     print(dp[i])
print(dp[-1][-1])