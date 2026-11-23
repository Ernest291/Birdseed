
"""
Stages/Scenes

Stage 1: Garden
Enemies: [Gnome, Butterfly, Flower, Snail, Bees, Earthworm] 
Final boss: Cat/Scarecrow or Gnome/Bee queen (depende if pira ka bee mapatay mo)  

Stage 2: Forest/Tree
Enemies: [Caterpillars, Squirrel, Stick insect, Mantis, Firefly]
Final Boss: [Treant(the tree itself if ma tree ta), Flying Squirrel, Firefly boss or sum idk way ko idea sa tree]

Stage 3: Sea
Enemies: [Crab, Fish/Flying Fish, Albatross, Seagull]
Final Boss: [Lighthouse, Pelican, Nemo/Dory]

Stage 4: Mountain
Enemies: [Hornet/Wasp, Mountain Goat, Golem, Eagle henchman]
Final Boss: [Bear, Bald Eagle]
"""
import random

scenes = { 
    'Stage1' : {
        'Enemies'      : { 
            'Gnome'    : {
                'HP'   : 60, 'Dmg'  : 20 },
            'Butterfly': { 
                'HP'   : 40, 'Dmg'  : 10},
            'Flower'   : {
                'HP'   : 45, 'Dmg'  : random.randint(12,17)},
            'Snail'    : { 
                'HP'   : 70, 'Dmg'  : 10},
            'Bees'     : {
                'HP'   : 40, 'Dmg'  : 13},
            'Earthworm': {
                'HP'   : 50,'Dmg'  : 20}
        },
        'Bosses'       : {
            'Cat'      : {
                'HP'   : 220, 'Dmg'  : 25},
            'Scarecrow': {
                'HP'   : 150, 'Dmg'  : 20*random.choice([1, 1.25])},
            'Gnome'    : {
                'HP'    : 170, 'Dmg'   : 27},
            'Queen_Bee': {
                'HP'   : 120, 'Dmg'  : 23*random.uniform(0.85, 1.1)}
        }
    },

    'Stage2' : {
        'Enemies'            : { 
            'Caterpillar'    : {
                'HP'         : 50, 'Dmg'        : 13 },
            'Squirrel'       : { 
                'HP'         : 60, 'Dmg'        : 20},
            'Stick Insect'   : {
                'HP'         : 40, 'Dmg'        : 15},
            'Mantis'         : { 
                'HP'         : 70, 'Dmg'        : 17*random.choice([1, 1.25])},
            'Firefly'        : {
                'HP'         : 55, 'Dmg'        : 15}
        },
        'Bosses'             : {
            'Treant'         : {
                'HP'         : 240, 'Dmg'        : 27},
            'Flying Squirrel': {
                'HP'         : 210, 'Dmg'        : 23},
            'Aspid'          : {
                'HP'         : 230, 'Dmg'        : random.randint(21,28)}
        }
    },
    'Stage3' : {
        'Enemies'         : { 
            'Crab'        : {
                'HP'      : 55,'Dmg'     : 18},
            'Flying Fish' : { 
                'HP'      : 60, 'Dmg'     : 23},
            'ALbatross'   : {
                'HP'      : 63, 'Dmg'     : 25},
            'Seagull'     : { 
                'HP'      : 63, 'Dmg'     : 25},
    },
        'Bosses'          : {
            'Lighthouse'  : {
                'HP'      : 300, 'Dmg'     : 24},
            'Pelican'     : {
                'HP'      : 264,'Dmg'     : 25},
            'Nemo'        : {
                'HP'      : 240, 'Dmg'     : 30}
        }
    },
    'Stage4' : {
        'Enemies'           : { 
            'Hornet'        : {
                'HP'        : 40, 'Dmg'       : 18},
            'Monutain Goat' : { 
                'HP'        : 70, 'Dmg'       : 20},
            'Pebblit'       : {
                'HP'        : 80, 'Dmg'       : 20},
            'Raven'           : { 
                'HP'        : 60, 'Dmg'       : 25},
            'HoneyGuide'    : {
                'HP'        : 60, 'Dmg'       : 20}
        },
        'Bosses'            : {
            'Pou'           : {
                'HP'        : 340, 'Dmg'       : 24},
            'Maurice'       : {
                'HP'        : 400, 'Dmg'       : 25},
        }}}
#def get_enemy(stage):
#     enemy = scenes[stage]['Enemies']
#
#     name, stats = random.choice(list(enemy.items()))
#
#     hp = stats['HP']
#     dmg = stats['Dmg']
#
#     if callable(dmg):
#         dmg = dmg()
#
#     return name, hp, dmg
#
# print(get_enemy('Stage1'))
#
# enemy, enemyHp, enemydmg = get_enemy('Stage1')
# print(enemy, enemyHp, enemydmg)
