from string import ascii_lowercase

def sort_letters(s):
    '''
    Description: Counting sort applied to sort letters
    
    Input: s     string, a phare with lenght - lowercase!

    Return: Sorting the letters in increasing order
    
    Complexity: O(n)
                Notice that any comparison search algorithm takes at least O(n log n)
                In this algorithm, I used counting sort that will reduce the time
                required to sort all the letters
    '''
    size = len(ascii_lowercase)

    return counting_sort(s,size, lambda x: ord(x)-ord('a'), lambda i: chr(ord('a')+i))


def counting_sort(s, buckets_size, id_fn, elem_fn):
    '''
    Description: Generic Counting sort 
    
    Input: s              string
           buckets_size   buckets quantity
           id_fn          function that convert an element in the corresponding bucket number
           elem_fn        function that convert a bucket number in an element

    Return: Sorted string s
    
    Complexity: O(n)
                Notice that this generic algorithm can sort any string of chars or numbers
    '''
    
    buckets = [0]*buckets_size
   
    # Iterate the string counting the letters apperance
    # O(n)
    for c in s:
        buckets[id_fn(c)] = buckets[id_fn(c)]+1

    # iterate the buckets to rebuild the sorted string    
    sorted_list = ''
    for i in range(buckets_size):
        sorted_list = sorted_list+elem_fn(i)*buckets[i]

    return sorted_list    



          



