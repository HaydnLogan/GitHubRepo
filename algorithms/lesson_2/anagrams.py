"""
Write a function to check whether two given strings are anagram of each other or not.
An anagram of a string is another string that contains the same characters, only the order
of  characters can be different.  For example, "abcd" and "dabc" are an anagram of each other.
"""

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)  # Ture False

def is_anagram2(ss1, ss2):
    if len(ss1) != len(ss2):
        return False

    count = {}  # dictionary with all the characters

    for letter in ss1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in ss2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for i in count:
        if count[i] != 0:
            return False

    return True



str1 = "abcccd"
str2 = "abccdc"
print(f'Anagrm 1:"', is_anagram(str1, str2))
print(f'Anagrm 2:"', is_anagram2(str1, str2))