# -*- coding: utf-8 -*-

import random
import unicodedata
import json
import threading
from normalize import *         #import normalize()
from checkindico import *       #import checkindico() 
from alreadywrited import *     #import wrote(), alreadywriten() and reset_mots_ecrits()
from bombtimer import *         
import socket

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#parameters
    #minimum bomb's time:
minimumTime = 5

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# liste_mots = all the valid words (dictionnary) in the game
with open('alpha1.1.json','r') as fichier_json:
    liste_mots = fichier_json.read()
print("mots dans dico:", len(liste_mots)) # returns the number of words in the dictionary

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

global endTurn

endTurn = False




# -_-_-_-_-
timing = False
t1 = threading.Timer(random.randint(minimumTime, minimumTime+7),set_timing_true)
t1.start()


while timing == False:
    mot_choisi = normalize(input("valeur = "))
    print("verif contenu variable mot_choisi : " + mot_choisi) #verif
    if checkindico(mot_choisi) == True:         #si mot dans dico
        if alreadywrited(mot_choisi) == False:  #et pas encore écrit
            print('mot correct')
            wrote(mot_choisi)
            endTurn = True
            break
        elif alreadywrited(mot_choisi) == True: #mais déja écrit
            print('mot déja écrit!')
        else:
            print('unless you are modifying the script, this is a bug! please report it to the spark team') #bug report, ne devrais pas arriver
            endTurn = True
            break
    elif checkindico(mot_choisi) == False:
        print("mot non existant dans la base de donnée actuellement")           #mot qui n'est pas dans le dictionnaire =>> à créer : fonction stocker mots faux pour les rajouter ensuite dans dico
    else:
        print('unless you are modifying the script, this is a bug! please report it to the Spark Team')     #bug report, ne devrais pas arriver
        endTurn = True
        break
    pass
print("compteur toujours en cours ? | ",t1.is_alive())