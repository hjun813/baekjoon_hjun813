# import sys
# import heapq

# n = int(sys.stdin.readline())
# people = []

# for i in range(n):
#     home, work = map(int, sys.stdin.readline().split())
#     heapq.heappush(people, (home, work))

# d = int(sys.stdin.readline())

# # print(n)
# # print(people)
# # print(d)
# maxresult = 0
# peopleCopy = []
# for i, j in people:
#     peopleCopy.append((i, j))



# while len(peopleCopy) > 1:

#     subway = (peopleCopy[0][0], peopleCopy[0][0] + d)
#     # print()
#     # print(subway[0],subway[1])
#     # print("Copy", peopleCopy)
#     count = 0
#     for i, j in peopleCopy:
#         if (i, j) in people:
#             continue
#         else:
#             heapq.heappush(people, (i, j))
#     # print("people:", people)


#     for v in range(len(people)):
#         # print("!!!", people[0][1])
#         if subway[0] <= people[0][0] and subway[1] >= people[0][0]:  # 집이 안에 있으면 직장도 있는지 체크
#             if subway[0] <= people[0][1] and subway[1] >= people[0][1]:  # 직장도 안에 있으면 카운트 +1
#                 # print("카운트")
#                 count += 1
#                 heapq.heappop(people)
#                 # print("people:", people)
#             else:
#                 heapq.heappop(people)
#                 # print("people:", people)
#         else:  # 집이 없으면 더볼필요 없음
#             break

#     # print(count)
#     maxresult = max(maxresult, count)

#     heapq.heappop(peopleCopy)


# if maxresult != 0:
#     print(maxresult)
# else:
#     print(0)
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


# 직장(work) 기준으로 정렬
people.sort(key=lambda x: x[1])

# 우선순위 큐 (heap)
heap = []
max_count = 0

# 슬라이딩 윈도우 방식으로 탐색
for home, work in people:
    # 현재 work 기준으로 d만큼 왼쪽 범위 설정
    start = work - d

    # heap에 home 추가
    heapq.heappush(heap, home)

    # 범위를 벗어난 집(home) 제거
    while heap and heap[0] < start:
        heapq.heappop(heap)

    # 현재 포함된 사람 수 업데이트
    max_count = max(max_count, len(heap))

print(max_count)
