# -*- coding: utf-8 -*-

import random
import unicodedata
import json
import threading
from normalize import *                                                                 #import normalize()
from checkindico import *                                                               #import checkindico() 
from alreadywrited import *                                                             #import wrote(), alreadywriten(), reset_mots_ecrits()
from bombtimer import *                                                                 #import countdown()

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# liste_mots = all the valid words (dictionnary) in the game
with open('alpha1.1.json','r') as fichier_json:
    liste_mots = fichier_json.read()
print("mots dans dico:", len(liste_mots))                                               # returns the number of words in the dictionary
mots_verif = open("mots_a_verif.txt", "a")

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

minimumTime = 10                                                                        #variable declaration

timing = False

endTurn = False

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

t1 = threading.Thread(target=countdown, args=(minimumTime,))

print('[console] début du tour')

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
mot_recherche = liste_mots[random.randint(0,len(liste_mots))]                           #randomly select one word in the dictionary
t1.start()
print(mot_recherche)                                                                    #the searched word (just temporary, for the tests)

while timing != True and endTurn != True:                                               #while the countdown and the turn aren't over 
    mot_choisi = normalize(input("valeur = "))
    if timing == True:                                                                  #check if the countdown is over (just in case)
        endTurn = True
        print('tour terminé par explosion de bombe')
    elif timing != True:                                                                #recheck if the countdown is over (just in case(we're never sure of anything))
        print(timing)
        if checkindico(mot_choisi) == True:                                             #check if the choosed word is in the dictionary
            if alreadywrited(mot_choisi) == False:                                      #check if the choosed word was already written
                print('mot correct et non écrit actuellement')
                wrote(mot_choisi)
                if mot_choisi == mot_recherche :                                        #check if the choosed word is the searched word
                    endTurn = True
                    print("c'était bien le mot " + mot_recherche + "! Bravo!")
            else:                                                                       #if the word was already written
                print('mot déja écrit!')
        else:                                                                           #if the word isn't in the dictionary
            print("ce mot n'est pas dans la base de données actuellement !")
            mots_verif.write(mot_choisi + ", ")                                         #append the "invalid word" in a manual checking to potentially append it in the dictionary
    else:                                                                               #shouldn't happen.
        print('bug')