import sys
input = sys.stdin.readline

N = int(input()) #(1~N-1 부품, N 완제품)
M = int(input())
recipe = {i: [] for i in range(1, N+1)}
basic = []

for _ in range(M):
    X, Y, K = map(int, input().split())
    recipe[X].append((Y, K)) # Y가 K개 필요

print(recipe)
# 딕셔너리가 빈것은 기본 부품임
recipeArr =[[0 for i in range(N+1)] for j in range(N+1)]


for i in range(1, N+1):
    if len(recipe[i]) == 0:
        basic.append(i)
        recipeArr[i][i] = 1
    else:
        for a, num in recipe[i]:
            recipeArr[i][a] = num
# 몇개 필요한지 다 적음


basic.sort()

for i in range(N+1):
    print(recipeArr[i])


for i in range(1, N+1):
    if i in basic:
        continue
    else:   #기본부품이 아닐때
        for j in range(1, N+1):
            if j in basic:
                continue
            else: #필요한게 기본 부품이 아닐때
                for k in range(1,N+1):
                    if recipeArr[j][k] > 0:
                        recipeArr[i][k] += recipeArr[j][k] * recipeArr[i][j]
                recipeArr[i][j] = 0
print()

for i in range(N+1):
    print(recipeArr[i])

for i in basic:
    print(i, recipeArr[N][i])