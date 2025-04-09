import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    volunteer = []
    for i in range(N):
        test1, test2 = map(int, input().split())
        volunteer.append((test1, test2))
    volunteer.sort()
    atleast = volunteer[0][1]
    answer = 1
    for i in range(1, N):
        if atleast > volunteer[i][1]:
            atleast = volunteer[i][1]
            answer += 1
        else:
            continue
    print(answer)
    