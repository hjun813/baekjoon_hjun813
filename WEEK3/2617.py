import sys
input = sys.stdin.readline
N, M = map(int, input().split())
#dfs 스택으로 풀었는데 시간초과

half = (N // 2) + 1
heavydic = {i: [] for i in range(1, N + 1)}  # 보다 무거운 것
lightdic = {i: [] for i in range(1, N + 1)}  # 보다 가벼운 것
result = []

# 타고 타고 들어가서 절반 + 1보다 많으면 카운트

for _ in range(M):
    heavy, light = map(int, input().split())
    lightdic[heavy].append(light)
    heavydic[light].append(heavy)
# print(heavydic)
# print(lightdic)

def heavydfs(v):
    stack = [v]
    count = -1

    while stack:
        node = stack.pop()
        count += 1
        for j in heavydic[node]:
            stack.append(j)

    if count >= half:
        result.append(v)

for i in range(1,N+1):
    heavydfs(i)


def lightdfs(v):
    stack = [v]
    count = -1

    while stack:
        node = stack.pop()
        count += 1
        for j in lightdic[node]:
            stack.append(j)

    if count >= half:
        result.append(v)

for i in range(1,N+1):
    lightdfs(i)

# print(result)
print(len(set(result)))