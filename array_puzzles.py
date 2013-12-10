#! /usr/bin/python


class arrayPuzzles:

    @staticmethod    
    def array_reverse(arr, start=0, end=-1):
        # Reverse arr starting from index start , ending at index end (inclusive)
        if (end == -1) or (end > len(arr)):
            end = len(arr)
        j = end - 1
        for i in range(end/2):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            j -= 1

