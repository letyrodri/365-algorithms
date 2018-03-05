import sys
import math
from string import ascii_lowercase

def anagram_palindrome(s):
    '''
    Description: Check if exists an anagram that it's a palindrome of s
 
    Input: s    input string

    Return: boolean - returns true if it exists
    
    Complexity: O(n)
                n is length of s

    '''
    qty = len(ascii_lowercase)
    store = [0]*qty

    for c in s:
        store[ord(c)-ord('a')] += 1

    odds = 0

    for i in range(qty):
        if store[i] % 2 == 1:
            odds += 1

    return odds < 2


