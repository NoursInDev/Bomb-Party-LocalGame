import json
from collections import Counter

with open("../dictionary/alpha1.1.json", "r") as f:
    words = json.load(f)

letters_2 = Counter()
letters_3 = Counter()

for word in words:
    for i in range(len(word) - 1):
        letters_2[word[i:i+2]] += 1
    for i in range(len(word) - 2):
        letters_3[word[i:i+3]] += 1

syllables = {}
for key, value in letters_2.items():
    if value >= 100:
        syllables[key] = value
for key, value in letters_3.items():
    if value >= 100:
        syllables[key] = value

with open("../dictionary/syllabes.json", "w") as f:
    json.dump(syllables, f)