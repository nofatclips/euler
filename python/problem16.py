#!/usr/bin/env python3.3
#
# Power digit sum
# Problem 16
# 03 May 2002
#
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2**1000?

print (sum(map(int,list(str(2**1000)))))