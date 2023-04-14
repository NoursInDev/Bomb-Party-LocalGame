# -*- coding: utf-8 -*-
import unicodedata
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
mots_ecrits = []
def wrote(add):
    """
        add the word in the "mots_ecrits" list
        -------
        INPUT : 
            add : str
                word to add
        --------
        OUTPUT :
            mots_ecrits : list
                list of all of the words already written 
    """
    #ajouter un mot écrit à la liste des mots écrits
    mots_ecrits.append(add)
    print(mots_ecrits)      #verification de la liste actuelle
    return mots_ecrits

def alreadywrited(check): #check si mot écrit a déja été écrit 
    """
            check if the word have already been written and return True if it is and False else
            -------
            INPUT : 
                check : str
                    word to check
            --------
            OUTPUT : 
                boolean
    """
    if check in mots_ecrits:    #demande si mot écrit est dans mots_ecrits ( remplie par fonction wrote() )
        return True
    else:
        return False

    
def reset_mots_ecrits():    #reset la liste de mots déja ecrit
    mots_ecrits = ()
    return mots_ecrits