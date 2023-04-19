# -*- coding: utf-8 -*-

import random
import unicodedata
import json
import threading
from normalize import *                                                                 #import normalize()
from checkindico import *                                                               #import checkindico() 
from alreadywrited import *                                                             #import wrote(), alreadywriten(), reset_mots_ecrits()
from multiprocessing import Value

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# liste_mots = all the valid words (dictionnary) in the game
with open('dictionary/alpha1.2.json','r') as fichier_json:
    liste_mots = json.load(fichier_json)
print("mots dans dico:", len(liste_mots))                                               # returns the number of words in the dictionary
mots_verif = open("mots_a_verif.txt", "a")

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

minimumTime = 5         #variable declaration
gameDifficulty = 500    #1 = min 1 word/syllable in data base

timing = False

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def gameTurn(wordbysyllable):                                                                   #GAME TURN FUNCTION -> BASIC FUNCTION OF ALL THE GAME
    endTurn = False
    bombTimer = random.randint(minimumTime, minimumTime+7)                                          #Duration generation
    t1 = threading.Timer(bombTimer, lambda: print('timing bomb initial : ', bombTimer))             #Set Timer in a thread

    print('[console] début du tour')                                                                #Console MSG
    
    with open('syllabes.json') as f:                                                                #Definition of the syllable
        data = json.load(f)                                                                             #By opening the file
    syllabe_list = [syllabe for syllabe, count in data.items() if count >= wordbysyllable]              #And selecting a random syllable with more or as many words per syllable as wordinsyllable
    random_syllabe = random.choice(syllabe_list)
    
    print('syllabe: ', random_syllabe)                                                              #Print the syllable
    # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    
    t1.start()                                                                                      #Start the Thread
    
    while t1.is_alive() == True and endTurn != True:                                            #while the countdown and the turn aren't over 
        mot_choisi = normalize(input("valeur = "))
        if t1.is_alive() == False:                                                              #check if the countdown is over (just in case)
            endTurn = True
            print('tour terminé par explosion de bombe')
        elif t1.is_alive() == True:                                                             #recheck if the countdown is over (just in case(we're never sure of anything))
            if random_syllabe in mot_choisi:                                                    #check if the syllable is contained in the chosen word
                if checkindico(mot_choisi, liste_mots) == True:                                             #check if the choosed word is in the dictionary
                    if alreadywrited(mot_choisi) == False:                                      #check if the choosed word was already written
                        print('mot correct et non écrit actuellement')
                        wrote(mot_choisi)
                        endTurn = True
                        break
                    else:                                                                       #if the word was already written
                        print('mot déja écrit!')
                else:                                                                           #if the word isn't in the dictionary
                    print("ce mot n'est pas dans la base de données actuellement !")
                    mots_verif.write(mot_choisi + ", ")                                         #append the "invalid word" in a manual checking to potentially append it in the dictionary
            else:
                print("ce mot ne contient pas la syllabe !")
        else:                                                                               #shouldn't happen.
            print('bug')
            endTurn = True
            break
    t1.join()
    print('verif : etat thread timer: ',t1.is_alive())
    mots_ecrits = []
    
if __name__ == '__main__':
    gameTurn(gameDifficulty)