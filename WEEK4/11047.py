import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = []
count = 0
for i in range(N):
    A.append(int(input()))

# A.sort(reverse=True)
# print(A)

for i in range(len(A)-1, -1, -1):
    while True:
        if K >= A[i]:
            count += (K // A[i])
            K = K % A[i]
            # print(K, A[i])
            
        else:
            break

print(count)
