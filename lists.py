# Define a list of names
names = ["Yoshi", "Mario", "Luigi", "Bowser"]

print(f"List of names: {names}")

# add element in the list
print("Append princess")
names.append("Princess")

# shows last element
print(f"Last element is: {names[-1]}")

print(f"Print out the whole list: {names}")
print(f"The last in alphabetical order is: {names[-1]}")

names.remove(names[-1])
print("last element removed")
print(names)
