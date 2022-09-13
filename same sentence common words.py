# Python program for the above approach
from collections import Counter

def removeCommonWords(sent1, sent2):
    sentence1 = list(sent1.split())
    sentence2 = list(sent2.split())
    frequency1 = Counter(sentence1)
    frequency2 = Counter(sentence2)

    word = 0
    for i in range(len(sentence1)):

        if sentence1[word] in frequency2.keys():
            sentence1.pop(word)

            word = word - 1
        word += 1

    word = 0

    for i in range(len(sentence2)):

        if sentence2[word] in frequency1.keys():
            sentence2.pop(word)

            word = word - 1

        word += 1

    print(*sentence1)
    print(*sentence2)
sentence1 = "sitha likes orange"
sentence2 = "orange is rich in anti_ dioxidents"

removeCommonWords(sentence1, sentence2)