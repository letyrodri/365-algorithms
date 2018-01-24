from math import floor
def is_palindrome(word):
    '''
    Detects if a word is a palindrome, for example neuquen
    
    It uses a n/2 iteration instead of n.

    Input: word - lowercase word

    Ouput: True - if word is a palindrome
           False - if word is not a palindrome

    Complexity: O(n/2) = O(n) 

    '''
    middle = floor(len(word)/2)

    for i in range(0,middle):
        if not (word[i] == word[len(word)-i-1]):
            return False

    return True 
