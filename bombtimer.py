# -*- coding: utf-8 -*-
import random
import unicodedata
import json
import threading
import time

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

    
def countdown(min):
    """
    countdown of the bomb
    -------
    INPUT :
        min : int
            the minimum time at the start of the countdown
    --------
    OUTPUT :
        timing : boolean
            true if the coutdown is at 0
    """
    global timing
    global endTurn
    timing=False
    endTurn=False
    temps = random.randint(min,min+7)
    print(temps)
    while endTurn==False and temps>0 : 
        temps -= 1
    if endTurn==False : 
        print("Kaboom, Time-up!")
        timing=True


        
if __name__=="__main__":
    countdown(5)