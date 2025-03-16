import sys

num = int(input())
test = [0] * (10001)

for i in range(num):
    test[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(int(test[i])):
        sys.stdout.write(str(i) + "\n")


# 어딘가 입력 받은거를 들고 있지 말고
# 입력으로 받는 숫자는 10000보다 작다
# 이게왜?
# 정렬된 상태로 출력
# 모든 수를 개별적으로 저장하지 않아도 그에 대한 정보만 표현할 수 있으면 되고,
# 정렬을 실제로 하지 않아도 정렬된 상태로 출력만
# 생각한 사람 개 똑똑하네 카운팅 정렬(계수 정렬)
