#! /usr/bin/python

from random import randint, shuffle
import unittest

class binSearchPuzzles:

    def __init__(self, init_arr):
        pass

    def binsearch(self, arr, x):
        start = 0
        end = len(arr)-1
        
        while start <= end:
            mid = (start + end) / 2
            if arr[mid] == x:
                return mid
            if x > arr[mid]:
                start = mid + 1
            else: 
                end = mid - 1

        return -1
        
class TestBinSearchPuzzles(unittest.TestCase):

    def setUp(self):    
        self.l = self.genRandomList(arrlen=5000, minval=0, maxval=10000, bUnique=True, bSorted=True)
        self.bsp = binSearchPuzzles(self.l)
        
    def genRandomList(self, arrlen=10, minval=0, maxval=10, bUnique=True, bSorted=False):
            if bUnique: 
                #If a list with unique is desired, use intermediate set() 
                s = set()
                # Avoid running into an infinite loop, if the range (maxval-minval) 
                # is not big enough to provide desired number of unique elements
                if (maxval - minval + 1) < arrlen:
                    return None
                # Now generate random numbers
                while len(s) < arrlen:
                    s.add(randint(minval, maxval))
                l = list(s)
            else:
                l = []
                #Uniqueness is not a criteria
                while len(l) < size:
                    l.append(randint(minval, maxval))
            #If sorted list is requested, comply
            if bSorted:
                l.sort()
            return l 

    def test_binarysearch(self):
        #Generate a shuffled list of all elements in the list to be searched
        #We want to search each element in a not orderly fashion
        lshuff = self.l[:]
        shuffle(lshuff)
        for x in lshuff:
            srchndx = self.bsp.binsearch(self.l, x)
            listndx = self.l.index(x)
            self.assertTrue(srchndx == listndx)

         
if __name__ == "__main__":
    unittest.main()
