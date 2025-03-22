import sys

N = int(sys.stdin.readline())
stick = []
count = 0
for i in range(N):
    stick.append(int(sys.stdin.readline()))

front = stick[-1]
for i in range(N-1,-1, -1):
    if stick[i] > front:
        front = stick[i]
        count += 1

print(count + 1)

