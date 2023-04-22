# -*- coding: utf-8 -*-
import json
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# liste_mots = tous les mots entrables
#              dans le jeu (mots valides)
def checkindico(check, wordList):
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
    if check in wordList:
        return True
    else:
        return False