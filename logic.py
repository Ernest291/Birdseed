from assets import words, arts
from hp_calc import damage 
import random
import os
import time

os.system("clear")

""" 
FUNCTIONS SECTION:
1. get_pool(pool)
2. print_srcn()
3. print_pool(pool)
4. get_input()
5. get_result(list_word_letters)
6. print_result(result)
7. get_points(result)


NOTES:
    - TODO:
      1. Make a health-points function 
      2. sprites 
      3. levels (random scenario) 
    - expect more functions lol~~
"""
def get_pool(pool):
    for _ in range(16):
        idx = random.choice(range(26))
        element = list(letters)[idx]
        pool.append(element)

def print_scrn(enemy_hp, points, my_hp,dmg):
    #57x11
    print(f""" 
    =========================================================
    [HP: {my_hp-dmg}]                           \t \t [HP: {enemy_hp-points}] 
    =========================================================
    [sprite]                                  [sprite]








    =========================================================
                        MAKE A WORD
    =========================================================
    """)

def print_pool(pool):
    for idx, letter in enumerate(pool):
        row = 1
        if (idx+1)%4==0 and idx!=0:
            print("\t", pool[idx].upper(), end="")
            print()
        else:
            print("\t",pool[idx].upper(), end=" ", flush=True)

    print()

def get_input(list_word_letters):
    str_word = input('\tMake a word: ') 
    list_word_letters.extend(str_word)
    return str_word

def get_result(list_word_letters):
    result = ""
    remaining = pool.copy()
    for letter in list_word_letters:
        if letter in pool and letter in remaining:
            result += letter
            remaining.remove(letter)
        else:
            result += "-"
            print(f"Letter {letter} not in the pool or already used.")
    return result

def print_result(result):
    if result in word_list:
        print(result)
    else:
        print("debug debug")

def get_points(result):
    points = []
    for l in result:
        points.append(letters.get(l))
    return sum(points)
""" 
LOGIC SECTION:

BASTA AH AMO NI HEHEHEH...

"""
points = 0
dmg = 0
enemy_hp = 30
my_hp = 30

while True:
    while enemy_hp-points>0:
        print("\t \t \t Stage 1 Level 1")
        pool = []
        letters = words.LETTERS
        word_list = words.ALL_WORDS
        list_word_letters = []

        get_pool(pool)
        print_scrn(enemy_hp, points, my_hp, dmg)
        print_pool(pool)
        get_input(list_word_letters)

        result = get_result(list_word_letters)
        print_result(result)

        if result in word_list:
            points += damage(get_points(result), len(result))

        input("press Enter to countinue...")
        dmg += random.randint(1,2)
        if my_hp-dmg<=0:
            exit("You Lose!")
            

        os.system("clear")

    enemy_hp +=40
    my_hp += 5
    while enemy_hp-points>0:
        print("\t \t \t Stage 1 Level 2")
        pool = []
        letters = words.LETTERS
        word_list = words.ALL_WORDS
        list_word_letters = []

        get_pool(pool)
        print_scrn(enemy_hp, points, my_hp, dmg)
        print_pool(pool)
        get_input(list_word_letters)

        result = get_result(list_word_letters)
        print_result(result)

        if result in word_list:
            points += damage(get_points(result), len(result))

        input("press Enter to countinue...")
        dmg += random.randint(2,3)
        if my_hp-dmg<=0:
            exit("You Lose!")

        os.system("clear")

    enemy_hp +=50
    my_hp += 10
    while enemy_hp-points>0:
        print("\t \t \t Stage 1 Level 3")
        pool = []
        letters = words.LETTERS
        word_list = words.ALL_WORDS
        list_word_letters = []

        get_pool(pool)
        print_scrn(enemy_hp, points, my_hp, dmg)
        print_pool(pool)
        get_input(list_word_letters)

        result = get_result(list_word_letters)
        print_result(result)

        if result in word_list:
            points += damage(get_points(result), len(result))

        input("press Enter to countinue...")
        dmg += random.randint(3,4)
        if my_hp-dmg<=0:
            exit("You Lose!")

        os.system("clear")
    

    break 

arts.win_ascii()
