# ***************************************************************************************************************************************************
#  *Author           : Ananthan.A - 286739
#  *File             : strop.py
#  *Title            : Python String Operations Module Development
#  *Description      : main file 
#  ****************************************************************************************************************************************************

import string
import itertools

# 1. getspan(s, ss) – Returns the start and end index (span) of substring ss in string s.
def getspan(s, ss):
    start = s.find(ss)
    if start == -1:
         return "Substring not found"
    return (start, start + len(ss) - 1)

# 2. reverseWords(s) – Reverses the order of words in s.
def reverseWords(s):
    words = s.split()
    return ' '.join(reversed(words))

# 3. removePunctuation(s) – Removes all punctuation from s.
def removePunctuation(s):
    return ''.join([char for char in s if char not in string.punctuation])

# 4. countWords(s) – Counts the number of words in s.
def countWords(s):
    words = s.split()
    return len(words)

# 5. characterMap(s) – Returns a dictionary with characters of s as keys and their frequencies as values.
def characterMap(s):
    return {char: s.count(char) for char in set(s)}

# 6. makeTitle(s) – Converts s to title case.
def makeTitle(s):
    return s.title()

# 7. normalizeSpaces(s) – Removes extra spaces, leaving only single spaces between words.
def normalizeSpaces(s):
    return ' '.join(s.split())

# 8. transform(s) – Reverses the string and swaps case.
def transform(s):
    return s[::-1].swapcase()

# 9. getPermutations(s) – Returns all permutations of the string s.
def getPermutations(s):
    return [''.join(p) for p in itertools.permutations(s)]
