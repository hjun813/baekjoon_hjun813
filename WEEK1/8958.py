testcase_num = int(input())

for i in range(testcase_num):
    testcase = str(input()).split("X")
    score = 0
    for j in range(len(testcase)):
        for k in range(len(testcase[j])):
            score = score + (k + 1)
    print(score)


# for i in range(testcase_num):
#     testcase.append(str(input()))
#     score = 0
#     a = testcase[i].split("X")
    
#     for j in range(len(a)):
#         for k in range(len(a[j])):
#             score = score + (k + 1)

#     print(score)

