"""
Given a non-empty string s, you may delete at most one character.  Judge wheter you can make it a palindrome.
The string will only contain lowercase characters a-z and it's not a palindrome.
Example: radarx -> True
radarxc -> False
"""

def is_palindrome(s):
    if s == s[::-1]:
        return False

    for i in range(len(s)):
        subs = s[:i] + s[i + 1:]
        print(subs)
        if subs == subs[::-1]:
            return True
    return False


print(is_palindrome("radar"))  # False, not almost, is actually
print(is_palindrome("radarx"))  # True (almost)
print(is_palindrome("radarxc"))  # False