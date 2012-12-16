#!/usr/bin/python  

# Problem 4
# 16 November 2001
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit number is
# 9009 = 91 × 99.

# Find the largest palindrome made from the product of
# two 3-digit numbers.

def isPalindromic (num):
    theNum=str(num)
    return theNum==theNum[::-1]

def maxPalindromic (low, high):
    ret = 0
    for a in range(high,low, -1):
        # print a
        for b in range(a-1, low-1, -1):
            c = a * b
            if c<ret: continue
            if isPalindromic(c): ret=c
    return ret

print maxPalindromic (100,999)