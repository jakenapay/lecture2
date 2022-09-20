# Define a list of names
names = ["Yoshi", "Mario", "Luigi", "Bowser"]

names.append("Princess")

# shows last element
print(names[0-1])

names.sort()
print(names)
print(f"The last in alphabetical order is: {names[0-1]}")

removedName = names[3]
names.remove(names[3])
print(names)
print(removedName)
