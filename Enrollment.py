# Using classes

class Enrollment():
    def __init__(self, slot):
        self.slot = slot
        self.students = []
    
    # Add student function
    def enroll(self, student):
        if not self.checkSlot():
            return False
        self.students.append(student)
        return True
    
    # Return if there's a slot
    def checkSlot(self):
        return self.slot - len(self.students)

    def enrolled(self, names):
        return self.students

enrollment = Enrollment(5)

students = []
for i in range(6):
    name = input("Enter student name: ")
    students.append(name)
    if enrollment.enroll(name):
        print(f"Student {students[i]} is successfuly enrolled.")
    else:
        print(f"Student {students[i]} is failed to enroll.")

print("List of passed in enrollment.")
for name in enrollment.students:
    print(f"{name} enrolled.")