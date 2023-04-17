# -*- coding: utf-8 -*-

import random
import unicodedata
import json
import threading
from normalize import *         #normalize()
from checkindico import *       #checkindico() 
from alreadywrited import *     #wrote(), alreadywriten(), reset_mots_ecrits()
from bombtimer import *

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# liste_mots = all the valid words (dictionnary) in the game
with open('alpha1.1.json','r') as fichier_json:
    liste_mots = fichier_json.read()
print("mots dans dico:", len(liste_mots)) # returns the number of words in the dictionary

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

minimumTime = 5

timing = False

endTurn = False

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

t1 = threading.Thread(target=countdown, args=(minimumTime,))

print('[console] début du tour')

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

t1.start()

while timing != True and endTurn != True:
    mot_choisi = normalize(input("valeur = "))
    print('contenu mot_choisi: ', mot_choisi)
    if timing == True:
        endTurn = True
        print('tour terminé par explosion de bombe')
        break
    elif timing != True:
        print(timing)
        if checkindico(mot_choisi) == True:
            if alreadywrited(mot_choisi) == False:
                print('mot correct et non écrit actuellement')
                wrote(mot_choisi)
                endTurn = True
                break
            else:
                print('mot déja écrit!')
        else:
            print("ce mot n'est pas dans la base de données actuellement !")
    else:
        print('bug')