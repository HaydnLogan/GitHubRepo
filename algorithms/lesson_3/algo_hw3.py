""" Algo HW3 (lesson 13)

Reverse a Statement
Build an algorithm that will print the given statement in reverse.
Example: Initial string = Everything is hard before it is easy
Reversed string = easy is it before hard is Everything
"""


def rev_statement(statement):
    word_list = statement.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    print(f'Reversed Statement: ', reversed_sentence)


s = (input('Input statement to be reversed: '))
l = rev_statement(s)


def permutation(word, first_char=None):
    if word == None or len(word) == 0:
        return []
    if len(word) == 1:
        return [word]

    result = []
    first_char = word[0]
    for sub_word in permutation(word[1:], first_char):
        result += insert(first_char, sub_word)
    return sorted(result)


def insert(ch, sub_word):
    arr = [ch + sub_word]
    for d in range(len(sub_word)):
        arr.append(sub_word[d:] + ch + sub_word[:d])
    return arr


n = (input('Input string you want to permutate: '))
print(permutation(n))


str5 = input("Input phrase for vowel and consonant count: ")
vowels = 0
consonants = 0
for i in str5:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
       i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
           vowels = vowels + 1
    else:
        consonants = consonants+1

print('Vowels:', vowels, ',', "Consonants:", consonants)
# How do I get the comma to appear closer to the vowels count?

print("The number of vowels:", vowels)
print("The number of consonants:", consonants)
