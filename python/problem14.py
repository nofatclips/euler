#!/usr/bin/env python3.3
#
# Longest Collatz sequence
# Problem 14
# 05 April 2002
#
# The following sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13,
# we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

class Collatz:

    def __init__(self, maxNum=100):
        self.maxNum = maxNum
        self.nums = [False for i in range(maxNum+1)]
        self.nums[0] = True
        self.nums[1] = True
        self.longestSequence = 1
        self.producesLongest = 1
        self.lastNumberChecked = 1

    # Set num as checked (True) or unchecked (False)
    def __setitem__ (self, num, value):
        if num<=self.maxNum:
            self.nums[num]=value
    
    # True if num has been checked
    def __getitem__ (self, num):
        return self.nums[num]
	
    def __iter__ (self):
        a = self.nextNumberToCheck()
        while a:
            yield a
            a = self.nextNumberToCheck()

    @staticmethod
    def _sequenceGenerator(n):
        yield n
        while n>1:
            n = (3*n+1) if n%2 else (n//2)
            yield n        

    def generateSequence(self, n):
        _generator = self._sequenceGenerator(n)
        cnt = 0
        for n in _generator:
            #print ("-> %i" % (n))
            self[n] = True
            cnt += 1
        return cnt

    def nextNumberToCheck(self):
        # Skip even values: there is always a sequence starting with
        # a lower odd number that includes the one starting with
        # an even one
        for i in range(self.lastNumberChecked, self.maxNum+1, 2):
            if not self[i]:
                self.lastNumberChecked = i
                return i
        return None

    def findLongestSequence(self):
        #current = self.nextNumberToCheck()
        #while (current):
        for sequence in self:
            #print (current)
            leng = self.generateSequence(current)
            if leng>self.longestSequence:
                self.longestSequence = leng
                self.producesLongest = current
            #current = self.nextNumberToCheck()
        return self.producesLongest

#print (Collatz(100000).findLongestSequence()) #77031
print (Collatz(1000000).findLongestSequence()) #837799
