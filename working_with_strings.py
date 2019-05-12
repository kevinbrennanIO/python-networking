a = "Some String"
b = "  more text  "
c = "$$$Strings$$$"
d = "this, is, a , string, of, words"


# prints first index of "S"
print(a.index("S"))

# prints a count of the letter "S"
print(a.count("S"))

# finds the sequeuence "ing"
print(a.find("ing"))

# finds the sequence "xpy"
print(a.find("xpy"))

# converts to lower case
print(a.lower())

# converts to upper case
print(a.upper())

# finds starts with "S"
print(a.startswith("S"))

# strips white space
print(b.strip())

# strinps specified character
print(c.strip("$"))

# replaces white space with no space
print(b.replace(" ", ""))

# splits a delimited list into an array
print(d.split(","))

# join the elements of a sting with "_" character
print("_".join(a))
