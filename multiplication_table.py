def multiplyTable(x, y):
    return x * y

n = int(input("Enter number you want: "))

for i in range(1, 11):
    print(f"{n} multiply by {i} is equal to {multiplyTable(n, i)}")