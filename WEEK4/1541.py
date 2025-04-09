import sys
input = sys.stdin.readline

arr = input().strip().split('-')
number = []
answer = 0

for item in arr:
    new = item.split('+')

    total = 0
    for i in new:
        total += int(i)

    number.append(total)

answer = number[0] 
if len(number) > 1:
    for i in range(1,len(number)):
        answer -= number[i] 

print(answer)