'''docstring in bulprint.py'''
import sys
from __init__ import print
try:
    if __name__ == '__main__':
        try:
            if len(sys.argv) == 3 or len(sys.argv) == 2:
                try:
                    print(sys.argv[1], time=float(sys.argv[2]))
                except IndexError:
                    print(sys.argv[1], time=0)
            else:
                raise IndexError()
        except Exception as e:
            print(f'Usage: {sys.executable} {__file__} <words to print> <time>\nExample: {sys.executable} {__file__} "hello" 4\nNot {sys.executable} {__file__} <something else>\nError: {type(e).__name__}')
except IndexError:
    pass