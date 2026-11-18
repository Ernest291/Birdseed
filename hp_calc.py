import random
import math

def damage(a , b):

    dmg = ((a*b)/2) + 5
           
    if random.randint(1,24) == 1: 
        critical = 1.5
    else:
        critical = 1

    is_crit = critical == 1.5
       
    rand = random.uniform(0.85, 1.1)
    final_damage = dmg*critical*rand
        
    return math.floor(final_damage) #, is_crit
    
#
# word_val = 0
# hp = float(input('EnHP: '))
# word_len = 0
#
# raw_dmg,is_crit = damage(word_len, word_val)
# dmg = int(raw_dmg)
#
#
# print("-" * 20)
#
# print('-', dmg)
# print('hp = ', hp-dmg)
#
# if is_crit:
#     print("it's a critical hit!")
