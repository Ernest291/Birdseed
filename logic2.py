""" 
[DUPLICATE]
"""

from assets import words
import random
import os

os.system("clear")
pool = []
letters = words.LETTERS
word_list = words.ALL_WORDS
list_word_letters = []

for _ in range(16):
    idx = random.choice(range(26))
    element = list(letters)[idx]
    pool.append(element)

#57x11
print(f""" 
=========================================================
[health? status?]                       [health? stats?] 
=========================================================
[sprite]                                  [sprite]








=========================================================
                    MAKE A WORD
=========================================================
""")

for idx, letter in enumerate(pool):
    row = 1
    if (idx+1)%4==0 and idx!=0:
        print("\t", pool[idx].upper(), end="")
        print()
    else:
        print("\t",pool[idx].upper(), end=" ", flush=True)

print()

str_word = input('Make a word: ') 
list_word_letters.extend(str_word)

result = ""
for letter in list_word_letters:
    if letter not in pool:
        print(f"Letter {letter} not in the pool.")
        result += "-"
    else:
        result += letter

if result in word_list:
    print(result)
else:
    print("debug debug")

points = []
for l in result:
    points.append(letters.get(l))

print(points)

