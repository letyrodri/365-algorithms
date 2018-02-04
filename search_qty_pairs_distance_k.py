def pairs(arr,k):
    '''
    Description: In a list of items, find how many pairs have k as distance 
    
    Input: arr list of items
           k   expected difference qty

    Return: the number of pairs
    
    Complexity: O(cost intersection len(arr) set)
                O(2*n) = O(n)
                where n is the len(arr)
    '''

    l2 = [x+k for x in arr]
    s1 = set(arr)
    s2 = set(l2)
    
    return len(s2.intersection(s1))
    
    

