#! /usr/bin/python

from random import randint, shuffle
import math 
import unittest

from array_puzzles import arrayPuzzles


class binSearchPuzzles:

    def __init__(self):
        pass


    def binsearch(self, arr, x, start=-1, end=-1):
        """
        arr :   A sorted array/list
        x   :   The element to find
        Task:   Perform binary search for element x in arr
        Returns:    Index of x in arr
                    If x not in arr, returns -1
        """

        if (start==-1) and (end==-1):
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


    def binsearch_rotated(self, arr, x):
        """
        arr :   A sorted and rotated array/list
        x   :   The element to find
        Task:   Perform binary search for element x in arr
        Returns:    Index of x in arr
                    If x not in arr, returns -1
        """
        start = 0
        end = len(arr)-1

        while start <= end:
            # If this segment is sorted, perform
            # regular binary search
            if arr[start] <= arr[end]: 
                return self.binsearch(arr, x, start, end)

            # Find the mid point
            mid = (start + end) / 2

            # By some good chance midpoint contains the element 
            # we are looking for then that's that
            if arr[mid] == x:
                return mid
        
            # Check if left section is sorted
            if arr[start] <= arr[mid-1]:
                # If it is sorted, check if x lies in-between
                if (x >= arr[start]) and (x <= arr[mid-1]):
                    # If so, perform binary search on it
                    return self.binsearch(arr, x, start, mid-1) 
                else:
                    # If element is not within sorted left-half, discard it
                    start = mid + 1   
            # Check if right section is sorted
            elif arr[mid+1] <= arr[end]:
                # If it is sorted, check if x lies in-between
                if (x >= arr[mid+1]) and (x <= arr[end]):
                    # If so, perform binary search on it
                    return self.binsearch(arr, x, mid+1, end) 
                else:
                    # If element is not within sorted right-half, discard it
                    end = mid - 1   


    def sqrt_binsearch(self, x):
        """
        Return Square root of x 
        If x is a negative (invalid), return -1
        If x is not a perfect square, return -1 (todo: fix this)
        """
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



    def find_tipping_point_linear(self, a, debug=False):
        """
        a is a rotated array  
        (Left-rotated or right-rotated ? Does not matter while solving this problem)
        The task of this routine is to return the tipping/pivot/transition 
        point of array a by searching linearly (in O(n) time complexity) 
        In simpler words, find the index of the largest integer in array a in 
        O(n) time complexity.
        """ 
        if(len(a) == 0): 
            return -1
    
        if(len(a) == 1):
            return 0
    
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                return (i-1)

        return i 



    def find_tipping_point_binsrch(self, a, debug=False):
        """
        a is a rotated array 
        (Left-rotated or right-rotated ? Does not matter while solving this problem)
        The task of this routine is to return the tipping/pivot/transition 
        point of array a in O(log n) time complexity. 
        In simpler words, find the index of the largest integer in array a
        in O(log n) time complexity.
        """
        start = 0
        end = len(a)-1
        # Remmeber the length of this array, we need it later twice
        arrlen = end-start+1

        if debug:
            print a
        
        while start <= end:
            # If this segment is already a sorted one,
            # the last index has the largest value
            if a[start] <= a[end]:
                return end


            # Find the mid-point
            mid = (start + end) / 2

            # Learned this neat trick here:
            # Video: How many times is a sorted array rotated?
            # Posted by user: mycodeschool
            # URL: http://www.youtube.com/watch?v=4qjprDkJrjY
            post_mid = (mid+1) % arrlen
            pre_mid = (mid-1+arrlen) % arrlen
    
            #if post_mid != (mid+1):
            #    print "post_mid adjusted to %d (err val = %d) len(a)=%d" % (post_mid, mid+1, len(a)),
            #if pre_mid != (mid-1):
            #    print "pre_mid adjusted to %d (err val = %d len(a)=%d)" % (pre_mid, mid-1, len(a)),
            
            if debug:
                print start, mid, end
            # Check if mid is the transition point
            if ((a[pre_mid] < a[mid]) and (a[post_mid] < a[mid])):
                return mid
            # Check if left half is not sorted, pivot is within there
            if a[start] > a[mid]:
                end = mid - 1;
            elif a[mid] > a[end]:
                start = mid + 1;
            else:
                return -1
            if debug:
                print start, mid, end
                print '-----'
        
        return -1

class TestBinSearchPuzzles(unittest.TestCase):

    def setUp(self):    
        self.l = self.genRandomList(arrlen=5000, minval=0, maxval=10000, bUnique=True, bSorted=True)
        self.bsp = binSearchPuzzles()
        
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
        lshuff = self.l[:]
        shuffle(lshuff) #Search elements in an un-orderly fashion
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

    def test_binarysearch_rotated(self):
        l = range(727,10001)+range(0,727) # Generate rotated arrays
        lshuff = l[:]
        shuffle(lshuff) #Search elements in an un-orderly fashion
        for x in lshuff:
            srchndx = self.bsp.binsearch_rotated(l, x)
            listndx = l.index(x)
            #print x, srchndx, listndx
            self.assertTrue(srchndx == listndx)
        # Now to try to find a number that is not present in the array
        unfound = max(l)+1
        srchndx = self.bsp.binsearch_rotated(l , unfound)
        self.assertTrue(srchndx == -1)
        # Now try to find in an array of length 1
        srchndx = self.bsp.binsearch_rotated([5], 5)
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
        start = randint(0,1000) # Let the smallest number be a random number
        arraylen = 10
        stop = start + arraylen + 1
        for r in range(arraylen):
            l = range(start, stop)
            l_expected = l[r:] + l[0:r] 
            # The first and the last iteration, 0 and arraylen,
            # do not produce any rotation really
            arrayPuzzles.array_rotate_right(l, r)
            self.assertTrue(l == l_expected)
        # Testing rotating 9 times the size of array
        l = range(start, stop)
        r = 9 * len(l)
        l_expected = l[:]
        arrayPuzzles.array_rotate_right(l, r)
        self.assertTrue(l == l_expected)


    def test_find_tipping_point(self):
        lengths = [ 1000+10, 3, 2, 1]  # Test with arrays of different sizes. 
                                       # Smaller sizes (3, 2, 1) are good to reveal
                                       # corner-cases
        dbgflg = False
        for length in lengths:
            for r in range(length):
                l = range(r,length)+range(0,r) # Generate rotated arrays
                tippt_bin = self.bsp.find_tipping_point_binsrch(l, debug=dbgflg)
                tippt_linear = self.bsp.find_tipping_point_linear(l, debug=dbgflg)
                #print l, 
                #print "a[%d] = %d" % (tippt, l[tippt])
                self.assertTrue(l[tippt_bin] == max(l))
                self.assertTrue(tippt_bin == (len(l)-1)-(r%len(l)))
                self.assertTrue(tippt_bin == tippt_linear)

        l = []
        tippt = self.bsp.find_tipping_point_binsrch(l)
        self.assertTrue(tippt == -1)
        #print l,
        #print "tippt = %d" % (tippt)


    


if __name__ == "__main__":
    unittest.main()
    
