###### LISTS ######

#initialise an empty list
list1 = [1, 2, "Hello", 12.5, -11]

print(type(list1)) # print the tyoe of a list
print(len(list1))  # print the length of a list
print(list1[2])    # print the value at index `2`

list1.append(100)
print(list1)

del list1[1]
# or
list1.pop(0)
#or
list1.remove("Hello")
print(list1)

print(max(list1))  # print the max value in list
print(min(list1))  # print the min value in list

list1.insert(2, "Python")  # insert value 'Python' at index '2'

list.append()
list.count()
list.sort()
list.reverse()