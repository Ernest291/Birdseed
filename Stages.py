
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
from assets import arts
scenes = { 
    'Stage1' : {
        'Enemies'      : { 
            'Gnome'    : {
                'HP'   : 60, 'Dmg'  : 20, 'sprite' : arts.vsGnome},
            'Butterfly': { 
                'HP'   : 40, 'Dmg'  : 10, 'sprite' : arts.vsButterfly},
            'Flower'   : {
                'HP'   : 45, 'Dmg'  : random.randint(12,17), 'sprite' : arts.vsFlower},
            'Snail'    : { 
                'HP'   : 70, 'Dmg'  : 10, 'sprite' : arts.vsSnail},
            'Bees'     : {
                'HP'   : 40, 'Dmg'  : 13, 'sprite' : arts.vsBees},
            'Earthworm': {
                'HP'   : 50,'Dmg'  : 20, 'sprite' : arts.vsEarthworm}
        },
        'Bosses'       : {
            'Cat'      : {
                'HP'   : 220, 'Dmg'  : 25, 'sprite' : arts.vsCat},
            'Scarecrow': {
                'HP'   : 150, 'Dmg'  : 20*random.choice([1, 1.25]), 'sprite' : arts.vsScarecrow},
            'Queen_Bee': {
                'HP'   : 120, 'Dmg'  : 23*random.uniform(0.85, 1.1), 'sprite': arts.vsQueenbee}
        }
    },

    'Stage2' : {
        'Enemies'            : { 
            'Caterpillar'    : {
                'HP'         : 50, 'Dmg'        : 13, 'sprite' : arts.vsCatterpillar },
            'Squirrel'       : { 
                'HP'         : 60, 'Dmg'        : 20, 'sprite' : arts.vsSquirrel},
            'Stick Insect'   : {
                'HP'         : 40, 'Dmg'        : 15, 'sprite' : arts.vsStickinsect},
            'Mantis'         : { 
                'HP'         : 70, 'Dmg'        : 17*random.choice([1, 1.25]), 'sprite' : arts.vsMantis},
            'Firefly'        : {
                'HP'         : 55, 'Dmg'        : 15, 'sprite' : arts.vsFirefly}
        },
        'Bosses'             : {
            'Treant'         : {
                'HP'         : 240, 'Dmg'        : 27, 'sprite': arts.vsTreant},
            'Flying Squirrel': {
                'HP'         : 210, 'Dmg'        : 23, 'sprite': arts.vsFlyingsquirrel},
            'Aspid'          : {
                'HP'         : 230, 'Dmg'        : random.randint(21,28), 'sprite' : arts.vsAspid}
        }
    },
    'Stage3' : {
        'Enemies'         : { 
            'Crab'        : {
                'HP'      : 55,'Dmg'     : 18, 'sprite': arts.vsCrab},
            'Flying Fish' : { 
                'HP'      : 60, 'Dmg'     : 23, 'sprite': arts.vsFlyingfish},
            'Albatross'   : {
                'HP'      : 63, 'Dmg'     : 25, 'sprite': arts.vsAlbatross},
            'Seagull'     : { 
                'HP'      : 63, 'Dmg'     : 25, 'sprite': arts.vsSeagull},
    },
        'Bosses'          : {
            'Lighthouse'  : {
                'HP'      : 300, 'Dmg'     : 24, 'sprite': arts.vsLighthouse},
            'Pelican'     : {
                'HP'      : 264,'Dmg'     : 25, 'sprite': arts.vsPelican},
            'Nemo'        : {
                'HP'      : 240, 'Dmg'     : 30, 'sprite': arts.vsNemo}
        }
    },
    'Stage4' : {
        'Enemies'           : { 
            'Hornet'        : {
                'HP'        : 40, 'Dmg'       : 18, 'sprite': arts.vsHornets},
            'Monutain Goat' : { 
                'HP'        : 70, 'Dmg'       : 20, 'sprite': arts.vsMountaingoat},
            'Pebblit'       : {
                'HP'        : 80, 'Dmg'       : 20, 'sprite': arts.vsPebblit},
            'Raven'           : { 
                'HP'        : 60, 'Dmg'       : 25, 'sprite': arts.vsRaven},
            'HoneyGuide'    : {
                'HP'        : 60, 'Dmg'       : 20, 'sprite': arts.vsHoneyguide}
        },
        'Bosses'            : {
            'Pou'           : {
                'HP'        : 340, 'Dmg'       : 24, 'sprite': arts.vsPou},
            'Maurice'       : {
                'HP'        : 400, 'Dmg'       : 25, 'sprite': arts.vsMaurice},
        }}}

