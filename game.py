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
mots_verif = open("mots_a_verif.exe", "a")

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

minimumTime = 10

timing = False

endTurn = False

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

t1 = threading.Thread(target=countdown, args=(minimumTime,))

print('[console] début du tour')

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
mot_recherche = liste_mots[random.randint(0,len(liste_mots))]
t1.start()
print(mot_recherche)

while timing != True and endTurn != True:
    mot_choisi = normalize(input("valeur = "))
    if timing == True:
        endTurn = True
        print('tour terminé par explosion de bombe')
    elif timing != True:
        print(timing)
        if checkindico(mot_choisi) == True:
            if alreadywrited(mot_choisi) == False:
                print('mot correct et non écrit actuellement')
                wrote(mot_choisi)
                if mot_choisi == mot_recherche : 
                    endTurn = True
                    print("c'était bien le mot " + mot_recherche + "! Bravo!")
            else:
                print('mot déja écrit!')
        else:
            print("ce mot n'est pas dans la base de données actuellement !")
            mots_verif.write(mot_choisi + ", ")
    else:
        print('bug')