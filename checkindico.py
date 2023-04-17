# -*- coding: utf-8 -*-
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# liste_mots = tous les mots entrables
#              dans le jeu (mots valides)
with open('alpha1.1.json','r') as fichier_json:
    liste_mots = fichier_json.read()

liste_alpha = []
with open('alpha1.1.json','r') as fichier_json:
    contenu_json = fichier_json.read()

liste_alpha = json.loads(contenu_json)      #entrer dans liste_alpha les caracteres autorisés

def checkindico(check):
    """
            check if the word is in the dictionnary and retun true if this word is in it and False if not
            -------
            INPUT :
                check : STR
                    word to check
            --------
            OUTPUT :
                boolean
    """
    if check in liste_mots:     #check if the word is in the dictionnary
        return True
    else:
        return False