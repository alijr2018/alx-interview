#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 100
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

#for n in range(1, 999999):
#   print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
