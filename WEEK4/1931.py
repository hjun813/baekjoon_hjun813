import sys
input = sys.stdin.readline

N = int(input())
timetable = []
result = 0

for _ in range(N):
    start, end = map(int, input().split())
    timetable.append((start, end))

timetable.sort(key=lambda x: (x[1], x[0]))

beforeEndT = 0

for i in range(N):
    startT, endT = timetable[i]
    if beforeEndT <= startT:
        result += 1
        beforeEndT = endT

print(result)   