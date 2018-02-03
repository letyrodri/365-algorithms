def partial_sorted_insertion_sort(arr):
    '''
    Description: Insert an element in a sorted array. 
    
    Input: arr sorted array for pos 0 to len(arr)-1, len(arr) elemmt to insert sorted
    Return: the position of e in sl
    
    Complexity: O(log n)
                n is length of sl
    '''

    
    to_insert = arr[len(arr)-1]
    i = len(arr)-2
    
    while (i >= 0):
        if arr[i] > to_insert: 
            arr[i+1] = arr[i]
            i = i-1
        else:
            arr[i+1] = to_insert
            break
    
    if i==-1:
        arr[0] = to_insert
    
    return arr

    
    