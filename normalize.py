# -*- coding: utf-8 -*-
import unicodedata
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

liste_mots = ["COUCOU","cc","bonjour"]      #temp list

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
    utilisateur_mot = utilisateur_mot.upper()                                                                   #capitalization
    utilisateur_mot = unicodedata.normalize('NFKD', utilisateur_mot).encode('ASCII', 'ignore').decode('ASCII')  #normalize = remove special characters and accents
    print ("mot choisi : "+ utilisateur_mot)                                                                    #print of the normalized word for a manual check
    return utilisateur_mot

if __name__=="__main__":                                                                                        #debug check
        normalize("évanouies")