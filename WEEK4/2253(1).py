import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cant = []

for _ in range(M):
    cant.append(int(input()))

cant.sort()

dp = [0] * (N+1)
for small in cant:
    dp[small] = -1
dp[1] = 0 
print(dp)

def jumpStone(now,jump):
    print(dp)
    if dp[N] == 0:
        if now < N:
            for i in range(1, -2, -1):
                if jump + i > 0:
                    print(now, jump+i)
                    if now+jump+i <= N:
                        if dp[now] != -1 and dp[now + jump + i] != -1:
                            dp[now + jump + i] = max(dp[now + jump + i], dp[now] + 1)
                            jumpStone(now+jump+i, jump+i)    
                        elif dp[now] == -1:
                            break
        else:
            return
    else:
        return

jumpStone(1, 0)

if dp[-1] != 0:
    print(dp[-1])
else:
    print(-1)

