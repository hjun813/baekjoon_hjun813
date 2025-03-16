textList = list(input().split(" "))
word_num = 0

for i in range(len(textList)):
    if textList[i] != "":
        word_num = word_num + 1

print(word_num)