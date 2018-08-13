#String types

x = "It is one of the string type passed"
y = 'It is the other type of the string passed'
z= """This is for the longer line
    it can break and continue to n number as the python automatically assigns it, thus the hassle of 
    declaration is not needed unlike other programming lanuages"""
#Here are the Sequence of Operations
print(z)
string1 = "Python"
string2 = 'Tutorial'

#Concatenation

print("Concatenating the values of string 1 and string 2", string1+string2)

#Repetition

print("Repeating the values of string to the n number of times as required",string2*2)

#Slicing

print("Slicing the string values ", string1[1:5] + string2[0:2])

#Indexing

print("Indexing the values in string 1 and string 2", string2[:-1])

print("Indexing the values in string 1 and string 2", string1[:-2])

#################################################################
#Type specific Method

#Find

print("Finding a specific character from the string", string1.find('hon'))

#Replace

print("Replacing the character with the new string value", string1.replace('Py','p'))

#Count

print("Count the characters in the string", string1.count('p', 0, 6))
""" The above count will display 0 as the python will see the exact match meaning case sensitive"""
print("Count the characters in the string", string1.count('P', 0, 6))

#Split

string3='P, Y, T, H, O, N'
print("Splitting the values of string 3 with , as the pointer",string3.split(','))

#Upper case Changement

print("Changing the string to upper case completely", string1.upper())

#Lower case Changement
print("Changing the string to lower case completely", string1.lower())

#Max and Min operator
"""Max will gives the value which is highest in alphabetical order whereas the 
min will give the value which is least in the alphabetical order"""
print("Finding the maximum alphabetical value in string 1", max(string1))
print("Finding the minimum alphabetical value in string 1", min(string1))

#TO check whether any alphabets available

print("Gives the boolean value if any alphabet is available in the mentioned string", string1.isalpha())

