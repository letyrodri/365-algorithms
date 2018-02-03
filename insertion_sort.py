
def insertion_sort(arr):
    '''
    Description: Insertion Sort
    
    Input: arr unsorted list
           
    Return: sorted arr
    
    Complexity: O(n^2)
                n is length of arr
    '''

    

    for i in range(1,len(arr)):
        while(i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1
    return arr       

