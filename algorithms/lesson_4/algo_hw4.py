"""
1.	Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]  """


nums = [1, 3, 5, 6, 4, 10, 2, 3]
ln = len(nums)
sn = sum(nums)
am = sn/ln
nl = []

for n in nums:
    if n < am:
        nl.append(n)

print(f"Input: {nums}")
print(f'Numbers below arithmetical mean:', nl)


""" 
2.	Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3   """


nums2 = [198, 3, 4, 9, 10, 9, 2]
print(f"\nLowest Elements of {nums2}:")
nums2.sort()
print(nums2[:2]) # print the first two.         start @ 0, go to 2
# print(nums2[2:]) # get rid of the first two.    start @ 2, go to end
# print(nums2)
# print(nums2[:-2]) # get rid of last two         start @ 0, go to -2 (2 before end)
# print(nums2[-2:]) # print the last two          start @ -2, go to end
