#Task A — Define the Student class
print("---Task A — Define the Student class---\n")

class Student:
    def __init__(self, name:str, group:str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade
    
    def __str__(self) -> str:
        return f"Student: {self.name}  ({self.group}; {self.average_grade})"
    
    def __repr__(self) -> str:
        return f"Student(name='{self.name}', group='{self.group}', average_grade={self.average_grade})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return (self.name == other.name 
                and self.group == other.group 
                and self.average_grade == other.average_grade)
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            raise TypeError(f"Cannot compare Student to an object of type {type(other).__name__}")
        return self.average_grade < other.average_grade

student = Student("John Smith", "Group-1", 42.5)

print("Outputting each attribute separately for the Student class:")
print(f"Name: {student.name}")
print(f"Group: {student.group}")
print(f"Average_grade: {student.average_grade}")

#Task B — Inspect internal structure
print("\n---Task B — Inspect internal structure---\n")

print(f"Print student.__dict__:\n {student.__dict__}")

student.__dict__['average_grade'] = 64.3

print(f"Show that the attribute value has changed after modify:\n {student.__dict__}")

#Task C — Implement __str__
print("\n-----Task C — Implement __str__-----\n")

#__str__ is implemented in the class located in task A

print(f"Demonstration of work __str__:\n{student}")

#Task D — Implement __repr__
print("\n-----Task D — Implement __repr__-----\n")

#__repr__ is implemented in the class located in task A

print(f"Demonstration of work __repr__:\n{repr(student)}")

#Task E — Implement equality (__eq__)
print("\n---Task E — Implement equality (__eq__)---\n")

#__eq__ is implemented in the class located in task A

student_2 = student
student_3 = Student("Jane Doe", "Group-1", 86.3)

print("Objects being compared:\n")
print(f"student: {repr(student)}")
print(f"student_2: {repr(student_2)}")
print(f"student_3: {repr(student_3)}\n")

print("Comparing objects:\n")
print(f"Equal students: {student == student_2}")
print(f"Different students : {student == student_3}")
print(f"Equal students: {student == "John Smith"}")

#Task F — Implement ordering (__lt__)
print("\n---Task F — Implement ordering (__lt__)---\n")

#__lt__ is implemented in the class located in task A

print("Objects being compared:\n")
print(f"student: {repr(student)}")
print(f"student_3: {repr(student_3)}\n")

print("Comparing objects by average_grade:\n")
print(f"Comparison with < works correctly: {student < student_3}")
print("Invalid comparisons are handled properly: ", end="")
try:
    print(student < 15.3)
except TypeError as e:
    print(f"Caught expected error: {e}")

#Task G — Sorting
print("\n-----Task G — Sorting-----\n")

students = [ student, student_3, Student("Jhon Doe", "Group-1", 84.3)]

print(" Before sorting: ")

for s in students:
    print(s)

students.sort()

print("\n After sorting: ")

for s in students:
    print(s)