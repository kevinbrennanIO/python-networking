x = "Cisco"
y = "Switch"

print(x + y)

print(x * 3)

# verify if a character is part of a string
print("o" in x)

print("o" not in x)

print("b" not in x)

model = "Cisco model: %s, %d  WAN slots, IOS %f "  % ("2600XM", 2, 12.4)
print(model)


model = "Cisco model: {}, {}  WAN slots, IOS {} "  .format("2600XM", 2, 12.4)
print(model)

#Strings - slicing
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

string1[5:15] #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
string1[5:] #slice starting at index 5 up to the end of the string
string1[:10] #slice starting at the beginning of the string up to, but NOT including, index 10
string1[:] #returns the entire string
string1[-1] #returns the last character in the string
string1[-2] #returns the second to last character in the string
string1[-9:-1] #extracts a certain substring using negative indexes
string1[-5:] #returns the last 5 characters in the string
string1[:-5] #returns the string minus its last 5 characters
string1[::2] #adds a third element called step; skips every second character of the string
string1[::-1] #returns string1's elements in reverse order
