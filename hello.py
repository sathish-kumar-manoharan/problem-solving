'''
Trynig my best comment
to test multi line comment

'''

from collections import defaultdict


numbers = [1, 0 , -3, 6, 5 , -9, 24]

print(list(filter(lambda x: x < 0 , numbers)))

def negative_numbers (number):
    return number < 0

print(list(filter(negative_numbers, numbers)))

print(list(filter(lambda x: x%2 == 0, numbers )))

def is_vowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

letters = ['a', 'b', 'd', 'e', 'i', 'p', 'm', 'g', 'j', 'o']

print(list(filter(is_vowel, letters)))

dictionary = defaultdict(list)

print("the dictionary is ", dictionary)
