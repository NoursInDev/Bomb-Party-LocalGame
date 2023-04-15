# -*- coding: utf-8 -*-
import random
import unicodedata
import json
import threading
import time

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def timer(minimum):
    """
        DESCRIPTION : 
            create and execute a countdown which have minimum of the minimum's variable and which is randomly increased for 0 to 7 seconds.
        --------
        INPUTS :  
            minimum : int
                the minimum of time what will be definded in the countdown 
    """
    timing = False
    bombtime = minimum + random.randint(0,7)    #définition du temps de la bombe
    while bombtime>0:
        time.sleep(1)
        bombtime -= 1
        
    timing = True

if __name__=="__main__":
    timer(15)