# Find the index of leftmost first repeated character.py
import sys

def leftmost(str_):
    fi = [-1] * 256
    res = sys.maxsize
    for i in range(0, len(str_)):
        ascii_ = ord(str_[i])
        if fi[ascii_] == -1:
            fi[ascii_] = i
        
        else:
            res = min(res, fi[ascii_])
    if res == sys.maxsize:
        return -1
    else:
        return res


print(leftmost(str_ = 'geeks'))
