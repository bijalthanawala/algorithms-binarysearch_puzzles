#! /usr/bin/python


class arrayPuzzles:

    @staticmethod    
    def array_reverse(arr, startndx=0, endndx=-1):
        # Reverse arr starting from index start , ending at index end (inclusive)
        if (endndx == -1) or (endndx >= len(arr)):
            endndx = len(arr)-1
        j = endndx
        for i in range((endndx-startndx+1)/2):
            tmp = arr[startndx+i]
            arr[startndx+i] = arr[j]
            arr[j] = tmp
            j -= 1

    @staticmethod
    def array_rotate_right(arr, n):
        # Rotate an array right (anticlock) by n elements 
        if ( n % (len(arr)) == 0) :
            print "Rotation size (%d) is mod of len of array (%d)" % n, len(arr)
            return
        n = n % len(arr)
        arrayPuzzles.array_reverse(arr, 0, n-1)
        arrayPuzzles.array_reverse(arr, n, len(arr)-1)
        arrayPuzzles.array_reverse(arr)
