"""
Lesson 11 Algo HW 2

1.	Split in Half.
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

"""

# str6 = "bbbbbcaaaaa"
def string(str6):
    c = len(str6)
    cd = c/2
    cr = round(cd,0)
    fh = str6[0:int(cr)]
    sh = str6[int(-cd):]
    print(f'Split and Swap =', sh + fh)


n = (input('Input string to be divided and swapped: '))
e = string(n)


"""
2.	Unique Characters in String.
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
Hint: https://www.w3schools.com/python/python_sets.asp
"""

def unique(str1):
    count = {}  # dictionary with all the characters

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for i in count:
        if count[i] != 1:
            return False

    return True

str1 = (input('Input string to test for uniqueness: '))
print(f'Is the string unique?', unique(str1))
