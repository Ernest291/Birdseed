from assets import words, arts
from assets.colors import BG_GRAY
from hp_calc import damage
from Stages import *
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
8. get_enemy(stage)
9. get_boss(stage)
8. get_enemy(stage)
9. get_boss(stage)


NOTES:
    - TODO:
      1. Make a health-points function 
      2. sprites 
      3. levels (random scenario) 
    - expect more functions lol~~
"""


def get_pool(pool):
    alphabet = list(words.LETTERS.keys())
    odds = [100 / pts for pts in words.LETTERS.values()]
    pool.extend(random.choices(alphabet, odds, k=16))


def print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite):
    # 57x11
    print(f""" 
                                                    ENEMY: {enemy}    
    =========================================================
    [HP: {my_hp - dmg}]                         \t \t [HP: {enemy_hp - points}] 
    =========================================================
{sprite}
    =========================================================
                        MAKE A WORD
    =========================================================
    """)


def print_pool(pool):
    for idx, letter in enumerate(pool):
        row = 1
        if (idx + 1) % 4 == 0 and idx != 0:
            print("\t", pool[idx].upper(), end="")
            print()
        else:
            print("\t", pool[idx].upper(), end=" ", flush=True)

    print()


def get_input(list_word_letters):
    str_word = input("\tMake a word: ").lower().strip()
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
        print(result.upper())
        print(result.upper())
    else:
        print("debug debug")


def get_points(result):
    points = []
    for l in result:
        points.append(letters.get(l))
    return sum(points)


def get_enemy(stage):

    enemy = scenes[stage]["Enemies"]

    name, stats = random.choice(list(enemy.items()))

    hp = stats["HP"]
    dmg = stats["Dmg"]
    sprite = stats["sprite"]

    if callable(dmg):
        dmg = dmg()

    return name, hp, int(dmg), sprite


def get_boss(stage):

    enemy = scenes[stage]["Bosses"]

    name, stats = random.choice(list(enemy.items()))

    hp = stats["HP"]
    dmg = stats["Dmg"]
    sprite = stats["sprite"]

    if callable(dmg):
        dmg = dmg()

    return name, hp, int(dmg), sprite


""" 
LOGIC SECTION:

BASTA AH AMO NI HEHEHEH...

"""
points = 0
dmg = 0
# enemy_hp = 30
my_hp = 200

# while True:
# STAGE 1
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage1")
while enemy_hp - points > 0:
    print("\t \t \t Stage 1 Level 1")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)
    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))
    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")
    os.system("clear")

# enemy_hp +=40
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage1")
while enemy_hp - points > 0:
    print("\t \t \t Stage 1 Level 2")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)
    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))
    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")
    os.system("clear")

# enemy_hp +=50
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage1")
while enemy_hp - points > 0:
    print("\t \t \t Stage 1 Level 3")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

points = 0
my_hp += 100
enemy, enemy_hp, enemy_dmg, sprite = get_boss("Stage1")
while enemy_hp - points > 0:
    print("\t \t \t Stage 1 BOSS")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# STAGE 2
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage2")
while enemy_hp - points > 0:
    print("\t \t \t Stage 2 Level 1")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# enemy_hp +=40
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage2")
while enemy_hp - points > 0:
    print("\t \t \t Stage 2 Level 2")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# enemy_hp +=50
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage2")
while enemy_hp - points > 0:
    print("\t \t \t Stage 2 Level 3")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

points = 0
my_hp += 150
enemy, enemy_hp, enemy_dmg, sprite = get_boss("Stage2")
while enemy_hp - points > 0:
    print("\t \t \t Stage 2 BOSS")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# STAGE 3
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage3")
while enemy_hp - points > 0:
    print("\t \t \t Stage 3 Level 1")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# enemy_hp +=40
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage3")
while enemy_hp - points > 0:
    print("\t \t \t Stage 3 Level 2")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# enemy_hp +=50
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage3")
while enemy_hp - points > 0:
    print("\t \t \t Stage 3 Level 3")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

points = 0
my_hp += 200
enemy, enemy_hp, enemy_dmg, sprite = get_boss("Stage3")
while enemy_hp - points > 0:
    print("\t \t \t Stage 3 BOSS")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")
# STAGE 4
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage4")
while enemy_hp - points > 0:
    print("\t \t \t Stage 4 Level 1")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# enemy_hp +=40
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage4")
while enemy_hp - points > 0:
    print("\t \t \t Stage 4 Level 2")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

# enemy_hp +=50
points = 0
my_hp += 50
enemy, enemy_hp, enemy_dmg, sprite = get_enemy("Stage4")
while enemy_hp - points > 0:
    print("\t \t \t Stage 4 Level 3")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")

points = 0
my_hp += 250
enemy, enemy_hp, enemy_dmg, sprite = get_boss("Stage4")
while enemy_hp - points > 0:
    print("\t \t Stage 4: The Final BOSS")
    pool = []
    letters = words.LETTERS
    word_list = words.ALL_WORDS
    list_word_letters = []

    get_pool(pool)
    print_scrn(enemy_hp, points, my_hp, dmg, enemy, sprite)
    print_pool(pool)
    get_input(list_word_letters)

    result = get_result(list_word_letters)
    print_result(result)
    result = get_result(list_word_letters)
    print_result(result)

    if result in word_list:
        points += damage(get_points(result), len(result))
    if result in word_list:
        points += damage(get_points(result), len(result))

    input("press Enter to countinue...")
    dmg += enemy_dmg
    my_hp -= dmg
    dmg = 0
    if my_hp - dmg <= 0:
        os.system("clear")
        arts.lose_ascii()
        input("Say your last words!\n")
        exit(f"\n \t ~me, 2026")

    os.system("clear")


arts.win_ascii()
