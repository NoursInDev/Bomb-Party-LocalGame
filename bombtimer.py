# -*- coding: utf-8 -*-
import random
import unicodedata
import json
import threading
import time

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def timer(minimum):
    """
        coucou les loulous
    """
    bombtime = minimum + random.randint(0,7)    #définition du temps de la bombe
    while bombtime>0:
        time.sleep(1)
        bombtime -= 1
        print(bombtime)
    timing = True

timer(15)