# -*- coding: utf-8 -*-
import unicodedata
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

liste_mots = ["COUCOU","cc","bonjour"]      #liste temporaire

def normalize(utilisateur_mot):
    """
                normalize and upper a word
        -------
        INPUT : 
                utilisateur_mot : str
                        word to normalize
        --------
        OUTPUT :
                utilisateur_mot : str
                        normalized word 
    """
    utilisateur_mot = utilisateur_mot.upper()                                                                   #mise en majuscules
    utilisateur_mot = unicodedata.normalize('NFKD', utilisateur_mot).encode('ASCII', 'ignore').decode('ASCII')  #normalise = enleve les caracteres speciaux et accents
    print ("mot choisi : "+ utilisateur_mot)                                                                    #verification du mot choisi
    return utilisateur_mot                                                                                      #retourne le mot choisi via normalize()