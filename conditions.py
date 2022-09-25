# # get user integer input
# n = int(input("Number: "))

# # else if of python
# # indention is a must
# if n > 0:
#     print(f"{n} is positive number")
# elif n < 0:
#     print(f"{n} is negative number")
# else:
#     print(f"{n} is neither positive nor negative")

# simple grading system
eng = float(input("Enter grade in english: "))
sci = float(input("Enter grade in science: "))
mat = float(input("Enter grade in math: "))
pro = float(input("Enter grade in programming: "))

totalSub = 4
ave = (eng + sci + mat + pro) / totalSub
print(f"Your average: {ave}")

if ave <= 74:
    print("You failed mah nig-")
elif ave >= 75 and ave <= 79:
    print("Your grade is below average")
elif ave >= 80 and ave <= 89:
    print("Your grade is average")
elif ave >= 90 and ave <= 100:
    print("Your grade is above average")
