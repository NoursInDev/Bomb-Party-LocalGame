# -*- coding: utf-8 -*-
import random
import unicodedata
import json
import threading
import time

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

    
def compte_a_rebours(min):      #timer bombe
    """
    countdown of the bomb
    -------
    INPUT :
        min : int
            the minimum time at the start of the countdown
    --------
    OUTPUT :
        none 
    """
    global timing
    timing = True
    for i in range(random.randint(min, min+7), 0, -1):      
        print(i)                                            #verif compte a rebours
        if timing == False:                                 #sensé arreter la fonction à timing == False
            break
        time.sleep(1)
    if timing == True:
        print("temps écoulé, Ka-Boom")
        print('etat de timing :', timing)
        
if __name__=="__main__":
    compte_a_rebours(5)