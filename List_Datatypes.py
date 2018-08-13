my_list = ['red','dad',3,'tall']
dummy_list=[4,5,6]
#Concatenation

print("Concatenating the values ", my_list +dummy_list)

#Repetition

print("Repeating the values ",my_list*2)

#Slicing

print("Slicing the string values ", my_list[1:2])

#Indexing

print("Indexing the values", my_list[-1])

#################################################################
#Type specific Method

#Append

print("Appending a specific character to the list", my_list.append('add'))

#Extend

print("Extending the character to the list", my_list.extend(['rat','dfa']))

#POP

print("POP will remove the top down from list", my_list.pop())

#Insert

print("Inserting the string in between the list, can be of any index",my_list.insert(2,'mom'))
