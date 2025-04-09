import sys
input = sys.stdin.readline
N, M = map(int, input().split())

half = (N // 2) + 1
graph1 = [[0 for i in range(N+1)] for j in range(N+1)]
count = 0

for _ in range(M):
    heavy, light = map(int, input().split())
    graph1[heavy][light] = 1

for i in range(N+1):
    print(graph1[i])

for k in range(1, 1+N):
    for i in range(1, 1+N):
        for j in range(1, 1+N):
            if graph1[i][k] == 1 and graph1[k][j] == 1:
                graph1[i][j] = 1
print()
for i in range(N+1):
    print(graph1[i])

for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        if graph1[i][j] == 1:
            tmp += 1
    if tmp >= half:
        count += 1

for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        if graph1[j][i] == 1:
            tmp += 1
    if tmp >= half:
        count += 1

print(count)