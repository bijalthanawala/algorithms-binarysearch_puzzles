#! /usr/bin/python

from random import randint, shuffle
import math 
import unittest

from array_puzzles import arrayPuzzles


class binSearchPuzzles:

    def __init__(self, init_arr):
        pass

    def binsearch(self, arr, x):
        # Find x in the list/array arr and return it's index in arr
        # If x not in arr, return -1
        start = 0
        end = len(arr)-1
        
        while start <= end:
            mid = (start + end) / 2
            if arr[mid] == x:
                #print "x=%d found at %d. arr[%d]=%d" % (x, mid, mid, arr[mid])
                return mid
            if x > arr[mid]:
                start = mid + 1
            else: 
                end = mid - 1

        #print "start=%d, end=%d. x=%d not found" % (start, end, x)
        return (-1)

    def sqrt_binsearch(self, x):
        # Return Square root of x 
        # If x is a negative (invalid), return -1
        # If x is not a perfect square, return -1 (todo: fix this)
        if not x:
            return x
        if x < 0:
            return -1
        start = 1 #1.0
        end = x
        while start <= end:
            mid = (start + end) / 2
            sqr = mid * mid
            if sqr == x:
                #print "sqrt(%d) = %d" % (x, mid)
                return mid
            if sqr < x:
                start = mid + 1
            else:
                end = mid -1
        #print "sqrt(%d) = %d" % (x, -1)
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
        # Now to try to find a number that is not present in the array
        unfound = max(self.l)+1
        srchndx = self.bsp.binsearch(self.l , unfound)
        self.assertTrue(srchndx == -1)
        # Now try to find in an array of length 1
        srchndx = self.bsp.binsearch([5], 5)
        self.assertTrue(srchndx == 0)

    def test_binsearch_sqrt(self):
       for x in range(50):
            sqrt = self.bsp.sqrt_binsearch(x) 
            if sqrt != -1:
                self.assertTrue(x == (sqrt * sqrt))
            else:
                #Confirm if we claim x to be not a perfect square, that that is so.
                self.assertFalse(math.ceil(math.sqrt(x)) == math.sqrt(x))
    
    def test_array_reverse(self):
        l = range(21) #Odd-sized array
        shuffle(l)
        l_native_reversed = l[:]
        arrayPuzzles.array_reverse(l)
        l_native_reversed.reverse()
        self.assertTrue(l_native_reversed == l)

        l.pop() #Even-sized array
        shuffle(l)
        l_native_reversed = l[:]
        arrayPuzzles.array_reverse(l)
        l_native_reversed.reverse()
        self.assertTrue(l_native_reversed == l)
        
    def test_array_rotate_right(self):
        arraylen = 10
        for r in range(arraylen):
            l = range(arraylen)
            l_expected = l[r:] + l[0:r] 
            # The first and the last iteration, 0 and arraylen,
            # do not produce any rotation really
            arrayPuzzles.array_rotate_right(l, r)
            self.assertTrue(l == l_expected)
        # Testing rotating 9 times the size of array
        l = range(10)
        r = 9 * len(l)
        l_expected = l[:]
        arrayPuzzles.array_rotate_right(l, r)
        self.assertTrue(l == l_expected)
         
if __name__ == "__main__":
    unittest.main()
    
