
txt = "I know how to use \"backslashes\""
# print(txt)
#
# print('o' in txt) # returns ture false
# print('y' in txt) # returns ture false
#
# print(txt[0:4]) # print by index
# print(txt[-2:]) # print by index from the end

str1 = "String1, test"
str2 = "String2"
str3 = "This is a string"
str4 = "     This is a string     "
str5 = "First argument is {} and second argument is {}"
str6 = "bbbbbcaaaaa"
mylist = ['This', 'is', 'a', 'string']

print(str1 + str2)
# print(str1[6])

# for d in str1:
#     print(d)
# print(len(str1))  # length of the string

# print(str1.lower()) #prints lower case
# print(str1.upper()) # prints upper case
# print(str3.split())

c = len(str6)
cd = c/2
cr = round(cd,0)

# print(str6[0:int(cr)])
# print(str6[int(-cd):])
# print(str6[int(-cd):], str6[0:int(cr)])

fh = str6[0:int(cr)]
sh = str6[int(-cd):]
list = [sh, fh]
print(''.join(list))



# print('-'.join(mylist))
# print(str4.strip())  # gets rid of extra spaces in beginning and end of string
# print(str3.replace('i', '1'))
# print(str3.find('T'))
# print(str5.format('one', 2))