import sys

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
except ValueError:
    print("Invalid input.")
    sys.exit(1)

try: 
    result = x / y
except ZeroDivisionError:
    print("Cannot be divided by 0.")
    sys.exit(1)

print(f"{x} / {y} is equals to {result}")