num = int(input())
word = []
sortedWord = []
finalWord = []

for i in range(num):
    word.append(input())

sortedWord = set(word)
finalWord = sorted(sortedWord, key=lambda x: (len(x), x))


for w in finalWord:
     print(w)

# for i in range(0, 50):
#     sortedWord = []
#     # if len(word) >= i+1:
#     for j in range(num):
#         # print(len(word[j]))

#         if len(word[j]) == i:
#             if sortedWord.count(word[j]) == 0:
#                 sortedWord.append(word[j])
#                 sortedWord.sort()
#     for v in range(len(sortedWord)):
#         finalWord.append(sortedWord[v])

# for i in range(len(finalWord)):
#     print(finalWord[i])


# num = int(input())
# word = set(input() for _ in range(num))  # 중복 제거하면서 입력받기

# # 길이순, 같은 길이면 사전순 정렬
# sorted_words = sorted(word, key=lambda x: (len(x), x))

# # 결과 출력
# for w in sorted_words:
#     print(w)
