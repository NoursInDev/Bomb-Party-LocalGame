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
#PARAMETRES
#Temps minimum à la bombe:
minimumTime = 5



# liste_mots = tous les mots entrables
#              dans le jeu (mots valides)
with open('alpha1.1.json','r') as fichier_json:
    liste_mots = fichier_json.read()

print("mots dans dico:", len(liste_mots)) # renvois nombre_mots


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

global timing
global endTurn
timing = False
endTurn = False

t1 = threading.Thread(target=timer, args=(5,))
t1.start()

mot_choisi = normalize()
print("verif contenu variable mot_choisi : " + mot_choisi) #verif

t1.join()
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-



while timing == False and endTurn == False:
    if checkindico(mot_choisi) == True:         #si mot dans dico
        if alreadywrited(mot_choisi) == False:  #et pas encore écrit
            print('mot correct')
            wrote(mot_choisi)
            endTurn = True
        elif alreadywrited(mot_choisi) == True: #mais déja écrit
            print('mot déja écrit!')
        else:
            print('unless you are modifying the script, this is a bug! please report it to the spark team') #bug report, ne devrais pas arriver
            endTurn = True
    elif checkindico(mot_choisi) == False:
        print("mot non existant dans la base de donnée actuellement")           #mot qui n'est pas dans le dictionnaire =>> à créer : fonction stocker mots faux pour les rajouter ensuite dans dico
    else:
        print('unless you are modifying the script, this is a bug! please report it to the Spark Team')     #bug report, ne devrais pas arriver
        endTurn = True
timing = False