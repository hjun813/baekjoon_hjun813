import sys
import heapq

# 입력 받기
n = int(sys.stdin.readline())
people = []

for _ in range(n):
    home, work = map(int, sys.stdin.readline().split())
    # 항상 home이 작은 값, work가 큰 값이 되도록 정렬
    people.append((min(home, work), max(home, work)))

d = int(sys.stdin.readline())

print('people',people)
# 직장(work) 기준으로 정렬
people.sort(key=lambda x: x[1])
print('peopleSort', people)
# 우선순위 큐 (heap)
heap = []
max_count = 0

# 슬라이딩 윈도우 방식으로 탐색
for home, work in people:
    # 현재 work 기준으로 d만큼 왼쪽 범위 설정
    print('home', 'work', home, work)
    start = work - d
    print('subway', start, work)
    # heap에 home 추가
    heapq.heappush(heap, home)
    print('heap!!', heap)

    # 범위를 벗어난 집(home) 제거
    while heap and heap[0] < start:
        heapq.heappop(heap)
        print('heap', heap)

    # 현재 포함된 사람 수 업데이트
    max_count = max(max_count, len(heap))
    print()

print(max_count)
