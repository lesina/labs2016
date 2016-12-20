n = int(input())
words = dict()
for i in range(n):
    word = input()
    if len(word) in words:
        words[len(word)].append(word)
    else:
        words[len(word)] = [word]
for i in sorted(words):
    print(i)
    blond_word = [word[::-1] for word in words[i]]
    blond_word.sort()
    for word in blond_word:
        print(word, word[::-1])
