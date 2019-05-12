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

