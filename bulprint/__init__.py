'''docstring in bulprint.py'''
import builtins
import time as timesleep
def print(words:str='', time:int|float=0):
    if time == 0:
        builtins.print(words)
    else:
        builtins.print(words)
        timesleep.sleep(time)
    return id({'words': words, 'time': time})