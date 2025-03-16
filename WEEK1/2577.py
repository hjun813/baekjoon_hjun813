A = int(input())
B = int(input())
C = int(input())

multNum = A * B * C


multNumList = list(map(int, str(multNum)))
for i in range(10):
    print(multNumList.count(i))


# for i in range(10):
#     globals()["a{}".format(i)] = 0
#     print('a{}'.format(i))
#     print(type('a{}'.format(i)))

# for i in range(len(multNumList)): 
#     for j in range(10):
        
#         if (int(multNumList[i]) == j):
#             "a{}".format(j) = "a{}".format(j) +1

# for i in range(10):
#     int(globals()["a{}".format(i)]) = 0

# for i in range(len(multNumList)):
#     for j in range(10):
#         if multNumList[i] == j: 
#             a{j} = 'a{j}' + 1