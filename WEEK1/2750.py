num = int(input())
test = []

for i in range(num):

    test.append(int(input()))

test.sort()
# print(test)


for i in range(len(test)):
    print(test[i])