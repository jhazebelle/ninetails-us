word_list = input().split()

word_freq = {}

for word in word_list:
    word_freq[word] = word_freq.get(word, 0) + 1

for word in word_list:
    print(f'{word} {word_freq[word]}')
