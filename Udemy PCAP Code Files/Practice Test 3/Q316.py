
text = "I'm gonna make him an offer he can't refuse"
words = text.split()
print(words)
# [["I'm", 'gonna', 'make', 'him', 'an', 'offer',
# 'he', "can't", 'refuse']
length = list(map(lambda word: len(word), words))
print(length)  # [3, 5, 4, 3, 2, 5, 2, 5, 6]
