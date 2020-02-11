# Exercise 4

# предложение разбивается на список слов, 
# затем создается список который содержит длину каждого слова.

sentence = 'It is raining cats and dogs'
words = sentence.split()
print(words) # ['It', 'is', 'raining', 'cats', 'and', 'dogs']

lengths = map(lambda word: len(word), words)
print(list(lengths)) # [2, 2, 7, 4, 3, 4]

# записать это одной строкой

print(list(map(lambda w: len(w), 'It is raining cats and dogs'.split())))
# [2, 2, 7, 4, 3, 4]

