# -*- coding: utf-8 -*-
import unicodedata
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
mots_ecrits = []
def wrote(add):
    """
            Fonction wrote(add) : ajoute suite de caractère entrée dans une liste
            ENTREE : ADD = Mot Entré
            SORTIE : LISTE (contiens tous les mots écrits jusqu'à présent)
    """
    #ajouter un mot écrit à la liste des mots écrits
    mots_ecrits.append(add)
    print(mots_ecrits)      #verification de la liste actuelle
    return mots_ecrits

def alreadywrited(check): #check si mot écrit a déja été écrit 
    """
            Fonction mot déja écrit ?
            ENTREE : Mot
            SORTIE : True/False
    """
    if check in mots_ecrits:    #demande si mot écrit est dans mots_ecrits ( remplie par fonction wrote() )
        return True
    else:
        return False

    
def reset_mots_ecrits():    #reset la liste de mots déja ecrit
    mots_ecrits = ()
    return mots_ecrits