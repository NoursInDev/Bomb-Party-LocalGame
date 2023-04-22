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
    mots_ecrits.append(add) #add the word in the "mots_ecrits" list
    print(mots_ecrits)      #print the already written words' list for a manual check
    return mots_ecrits

def alreadywrited(check):
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
    if check in mots_ecrits:
        return True
    else:
        return False

    
def reset_mots_ecrits():
    """
        reset the list of the aldready written's words
        --------
        OUTPUT :
            mots_ecrits : list
                cleared aldready written's words list 
    """
    mots_ecrits = []