# -*- coding: utf-8 -*-
import unicodedata
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

liste_mots = ["COUCOU","cc","bonjour"]      #liste temporaire

def normalize():
    """
            Fonction Normalise + MAJ
            ENTREE : Môt
            SORTIE : MOT
    """
    utilisateur_mot = input("valeur = ")                                                                        #demande le mot à entrer
    utilisateur_mot = utilisateur_mot.upper()                                                                   #mise en majuscules
    utilisateur_mot = unicodedata.normalize('NFKD', utilisateur_mot).encode('ASCII', 'ignore').decode('ASCII')  #normalise = enleve les caracteres speciaux et accents
    print ("mot choisi : "+ utilisateur_mot)                                                                    #verification du mot choisi
    return utilisateur_mot                                                                                      #retourne le mot choisi via normalize()