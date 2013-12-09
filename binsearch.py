#! /usr/bin/python

from random import randint
from random import shuffle

class array_puzzles:
    arr = []

    def __init__(self, init_arr):
        self.arr = init_arr[:]
        #print self.arr

    def printarr(self):
        print self.arr

    def binsearch(self, x):
        start = 0
        end = len(self.arr)-1
        
        #print "Looking for ", x
        while start <= end:
            mid = (start + end) / 2
            if self.arr[mid] == x:
                return mid
            if x > self.arr[mid]:
                start = mid + 1
            else: 
                end = mid - 1

        return -1
        
    

if __name__ == "__main__":
    s = set()
    while len(s) < 5000:
        s.add(randint(0,10000))
    l = list(s)
    l.sort()
    ap = array_puzzles(l)
    lshuff = l[:]
    shuffle(lshuff)
    #print lshuff
    for x in lshuff:
        srchndx = ap.binsearch(x+5000)
        listndx = l.index(x)
        print x, " found at ", srchndx, ". Actual index = ", l.index(x)
        if srchndx != listndx:
            print x, " found at ", srchndx, ". Actual index = ", l.index(x)
            break
    else:
        print "Pass"

         
