# -*- coding: utf-8 -*-

import random
import unicodedata
import json
import threading
from normalize import *         #import normalize()
from checkindico import *       #import checkindico() 
from alreadywrited import *     #import wrote(), alreadywriten() and reset_mots_ecrits()
from bombtimer import *         #import compte_a_rebours()

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
t1 = threading.Thread(target=compte_a_rebours, args=(1,))
t1.start()


while timing == False and endTurn == False:
    mot_choisi = normalize(input("valeur = "))
    print("verif contenu variable mot_choisi : " + mot_choisi) #print the choosed word for a manual check
    if timing == True:
        print('la bombe a déja explosé !')
        break
    elif timing == False:
        if checkindico(mot_choisi) == True:         #check if the choosed word is in the dictionnary 
            if alreadywrited(mot_choisi) == False:  #and if it wasn't already writen
                print('mot correct')
                wrote(mot_choisi)
                endTurn = True
                break
            elif alreadywrited(mot_choisi) == True: #if the choosed word is in the dictionnary but was already written
                print('mot déja écrit!')
            else:
                print('unless you are modifying the script, this is a bug! please report it to the spark team') #bug report, should not happen
                endTurn = True
                break
        elif checkindico(mot_choisi) == False:      #if the choosed word isn't in the dictionnary
            print("mot non existant dans la base de donnée actuellement")           #mot qui n'est pas dans le dictionnaire =>> à créer : fonction stocker mots faux pour les rajouter ensuite dans dico
        else:
            print('unless you are modifying the script, this is a bug! please report it to the Spark Team')     #bug report, should not happen
            endTurn = True
            break
        pass
    else:
        print('unless you are modifying the script, this is a bug! please report it to the Spark Team')     #bug report, should not happen
        endTurn = True
        break