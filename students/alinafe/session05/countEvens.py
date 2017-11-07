#!/usr/bin/env python3

nums =[1,2,3,4,5,6,56565,4,5656]
def count_evens(nums):
   return len([x for x in nums if not x%2])

print(count_evens(nums))
