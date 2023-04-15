# -*- coding: utf-8 -*-
import random
import unicodedata
import json
import threading
import time

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

    
def compte_a_rebours(min):
    global timing
    bombTime = random.randint(min, min+7)
    time.sleep(bombTime)
    set_timing_true()
    
def set_timing_true():
    global timing
    timing = True
    print("timing terminé ? | ",timing)

if __name__=="__main__":
    compte_a_rebours(5)