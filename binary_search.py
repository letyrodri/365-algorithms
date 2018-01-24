from math import floor

def binary_search(sl,e):
    '''
    Description: Binary Search (recursive implementation)
    
    Input: sl    sorted list
           e     element in the list

    Return: the position of e in sl
    
    Complexity: O(log n)
                n is length of sl
    '''

    # This method is defined only if e is in l, but just loop for ever if it didn't
    
    middle = floor(len(sl) / 2)

    if sl[middle] == e:
        return middle
    else:
        if sl[middle] > e:
            return binary_search(sl[0:middle],e)
        else:
            return middle+binary_search(sl[middle:len(sl)], e)


