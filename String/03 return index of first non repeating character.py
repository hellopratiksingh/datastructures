# Return index of first non repeating Character of a string:
import sys

def firstNonRepeating(str):
    fi = [-1] * 256
    res = sys.maxsize
    for i in range(0, len(str)):
        ascii_ = ord(str[i])
        if fi[ascii_] == -1:
            fi[ascii_] = i

        else:
            fi[ascii_] = -2

    for i in range(0, 256):
        if fi[i] >= 0:
            res = min(res, fi[i])

    if res == sys.maxsize:
        return -1
    else:
        return res



print(firstNonRepeating('geeksforgeeks'))
