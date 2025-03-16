import sys
num = int(input())
test = []

for i in range(num):

    test.append(int(sys.stdin.readline()))


# def quickSort(arr):
#     if len(arr) <= 1: #종료조건
#         return arr
    
#     pivot = arr[0]
#     left =  [x for x in arr[1:] if x < pivot] 
#     right =  [x for x in arr[1:] if x >= pivot]

#     return quickSort(left) + [pivot] + quickSort(right)

# sortedNum = quickSort(test)

for i in sorted(test):
    sys.stdout.write(str(i) + '\n')