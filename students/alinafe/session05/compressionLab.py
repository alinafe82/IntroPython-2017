#!/usr/bin/env python3
nums =[1,2,3,4,5,6,56565,4,5656]
def count_evens(nums):
   return len([x for x in nums if not x%2])

print(count_evens(nums))


#Print the dict by passing it to a string format method, so that you get something like:
#“Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

comprehension = [ word for word in food_prefs.values()]

comprehension[0] + " is from "+ comprehension[1]+", and he likes"+comprehension[2]+"cake,"+comprehension[3]+" fruit,"+comprehension[4]+" salad, and"+
comprehension[5]+" pasta"
'Chris is from Seattle, and he likeschocolatecake,mango fruit,greek salad, andlasagna pasta'

compalt =    "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta"


#Using a list comprehension, build a dictionary of numbers from zero to fifteen and the
#hexadecimal equivalent (string is fine). (the hex() function gives you the hexidecimal
hexadec = {val: hex(val) for val in range(16)}

#Using the dictionary from item (1): Make a dictionary using the same keys but with
#the number of ‘a’s in each value. You can do this either by editing the dict in place, or
#making a new one. If you edit in place make a copy first!
a = {s: v.count('a') for s, v in food_prefs.items()}

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
#Do this with one set comprehension for each set.


 s2 = {s for s in range(21) if s % 2 == 0}
 s3 = {s for s in range(21) if s % 3 == 0}
 s4 = {s for s in range(21) if s % 4 == 0}
#What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
#create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.

#loop through that sequence to build the sets up – so no repeated code. you will end up with a
#list of sets – one set for each divisor in your sequence.

divisors = range(1, 8)
sets = []
for divisor in divisors:
    sets.append({s for s in range(21) if s % divisor == 0})

sets
[{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20},
 {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20},
 {0, 3, 6, 9, 12, 15, 18},
 {0, 4, 8, 12, 16, 20},
 {0, 5, 10, 15, 20},
 {0, 6, 12, 18},
 {0, 7, 14}]
#The idea here is that when you see three (Or more!) lines of code that are almost identical,
#then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.
#Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)
