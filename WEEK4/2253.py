import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cant = []

for _ in range(M):
    cant.append(int(input()))


cant.sort()

jump = 1
count = 0
current = 1

while True:
    # print(current, jump)
    # print(count)
    # print()
    if current < N:
        if jump != 0:

            if current + jump <= N:
                current += jump
                if current in cant:
                    current -= jump
                    jump -= 1 # 문제에서 감소는 한번밖에 안됨
                    continue
                else:
                    jump += 1
                    count += 1
                    continue
            else:
                count += 1
                break

        elif jump == 0:
            count = -1
            break
    elif current == N:
        break
    else:
        count = -1
        break

print(count)