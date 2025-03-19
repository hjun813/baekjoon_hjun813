num = int(input())
numList = []
numList = list(map(int, (input().split())))
used = [False] * num
newNum = [0] * num
# minusBet = [0] * num
minusN = [0] * num
total = []

# count = 0
# print(numList)
# print(count)

def minusBetF(arr):
    global minusN
    for i in range(len(arr)-1):
        minusN[i] = arr[i] - arr[i+1]
        if minusN[i]<0:
            minusN[i] = -minusN[i]
    total.append(sum(minusN))
    # print(sum(minusN))



def between(A, n, num):

    for i in range(num):

        if not used[i]:
            
            newNum[n] = numList[i]

            if n == num - 1:
                # calculateCost(trip)
                # print(newNum)
                minusBetF(newNum)

            else:
                used[i] = True
                between(A + i, n + 1, num)
                used[i] = False



between(0, 0,num)
print(max(total))