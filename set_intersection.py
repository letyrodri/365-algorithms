def set_intersection(s1,s2):
    '''
    Description: Write the insertion of to set, maximum cost O(n*m)
                 m is len(s2), n is len(s1)
    
    Input: s1, s2 - set to be intersected
    
    Return: Set intersection
    
    Complexity: O(n*m) worst case
                m is len(s2), n is len(s1)
    '''

    res = set()

    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                res.add(e1)
        
    return res


