import sys

# 입력 받기
M, N, L = map(int, sys.stdin.readline().split())
postionP = list(map(int, sys.stdin.readline().split()))
animal = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 사냥터 위치 정렬
postionP.sort()

# 이진 탐색 함수
def binarySearch(a):
    start, end = 0, M - 1
    while start < end:
        mid = (start + end) // 2
        if postionP[mid] < a:
            start = mid + 1
        else:
            end = mid
    return start

count = 0

for x, y in animal:
    idx = binarySearch(x)
    print('animal', x, y)
    print('idx', idx)
    closest = postionP[idx]

    if idx > 0:  # 왼쪽 사냥터도 비교 가능하면 비교
        left = postionP[idx - 1]
        if abs(left - x) < abs(closest - x):
            closest = left

    if abs(closest - x) + y <= L:
        count += 1
    
    print()

print(count)