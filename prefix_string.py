#!/bin/python3

import sys
from string import ascii_lowercase

def prefix_string(s1, s2):
    '''
    Description: Given two strings, a and b , determine if they share a common substring.
 
    Input: s1,s2    input string

    Return: boolean - returns true if it exists
    
    Complexity: O(n+m)
                n is length of s1
                m is the length of s2

                It could be optimized? 
    '''

    val = [0]*len(ascii_lowercase)
    
    for c in s1:
        idx = ord(c)-ord('a')
        if val[idx] == 0:
            val[idx] = 1
    
    for c in s2:
        idx = ord(c)-ord('a')
        if val[idx] == 1:
            val[idx] = 2

    return len([x for x in val if x == 2]) > 0
   
