from typing import Optional, Type, Any, Literal
from types import TracebackType

class GradeDescriptor:
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self._name: str = '_' + name

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name)

    def __set__(self, instance: Any, value: float) -> None:
        if not (0.0 <= value <= 100.0):
            raise ValueError(f"Grade must be between 0 and 100. Got: {value}")
        setattr(instance, self._name, float(value))

class Student:
    grade: GradeDescriptor = GradeDescriptor()

    def __init__(self, name:str, group:str, grade: float):
        self.name = name
        self.group = group
        self.grade = grade
    
    def __str__(self) -> str:
        return f"Student: {self.name}  ({self.group}; {self.grade})"
    
    def __repr__(self) -> str:
        return f"Student(name='{self.name}', group='{self.group}', grade={self.grade})"

student_1 = Student("John Smith", "Group-1", 42.5)
student_2 = Student("John Doe", "Group-2", 66.6)
student_3 = Student("Jane Doe", "Group-1", 83.2)

#Task A — Iteration
print("---Task A — Iteration---\n")

class StudentCollectionIterator:
    def __init__(self, students_list: list[Student]):
        self._students = students_list
        self._index = 0

    def __iter__(self) -> "StudentCollectionIterator":
        return self

    def __next__(self) -> Student:
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        else:
            raise StopIteration


class StudentCollection:
    def __init__(self, students: Optional[list[Student]] = None) -> None:
        self._students: list[Student] = students if students is not None else []

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def __iter__(self) -> StudentCollectionIterator:
        return StudentCollectionIterator(self._students)
    
    def __enter__(self) -> "StudentCollection":
        print(">>> Entering the context: StudentCollection is initialized and ready.")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        _exc_tb: Optional[TracebackType]
    ) -> Literal[False]:
        print("<<< Exiting the context: Performing cleanup operations.")

        if exc_type is not None:
            print(f"    [!] Context Manager caught: {exc_type.__name__} - {exc_val}")
        return False


collection = StudentCollection()
collection.add_student(student_1)
collection.add_student(student_2)
collection.add_student(student_3)


print("Iterating through the collection:\n")
for student in collection:
    print(student)

print("\n[Explanations]")

print('''We see that the `for` loop successfully iterates through our custom `StudentCollection` object, 
      printing each `Student` one by one without needing index variables like `i=0`.''')

print('''It works because we implemented the Iterator Protocol. When the `for` loop starts, 
      Python calls `iter(collection)`, which triggers our `__iter__` method and returns a 
      `StudentCollectionIterator` object. Then, on each step, Python calls `next()` on this iterator. 
      Our `__next__` method returns the next student and updates the internal state until it raises 
      `StopIteration` to gracefully end the loop.''')

#Task B — Context Manager
print("\n---Task B — Context Manager---\n")

#  __enter__ and __exit__ in task A

print("*** Normal Execution ***")
with StudentCollection() as collection:
    collection.add_student(Student("John Smith", "Group-1", 42.5))
    print("    Working inside the context...")
print("Context block finished successfully.\n")


print("*** Error Execution ***")
try:
    with StudentCollection() as collection:
        print("    Working inside the context...")
        raise ValueError("Simulated unexpected error!")
        print("    This line will never be reached.")
except ValueError as e:
    print(f"Exception caught outside the context: {e}")

print("\n[Explanations]")

print('''1. In Normal Execution, the program prints '>>> Entering...' before executing the block, and '
      <<< Exiting...' right after finishing it.''')
print('''2. In Error Execution, an exception (`ValueError`) is intentionally raised inside the `with` block.
       Despite the crash, the '<<< Exiting...' message is STILL printed before the exception is passed to 
      the `except` block.''')

print('''The `with` statement evaluates the `StudentCollection` object and automatically calls 
      its `__enter__()` method, assigning the returned value to the `collection` variable. Once the block 
      of code inside the `with` statement finishes—whether naturally or due to a crashed state (exception)
      — Python guarantees that the `__exit__()` method is called. This provides a safe, fail-proof mechanism 
      for resource management and cleanup.''')

#Task C — Descriptor
print("\n-----Task C — Descriptor-----\n")

# GradeDescriptor created before Student

print("Creating a student with a valid grade (85.0)...")
student_c = Student("Test Student", "CS-41", 85.0)
print(f"   Success: {student_c}")

print("\n Attempting to set an invalid grade (120) [Example usage]...")
try:
    student_c.grade = 120.0
    print("   This line will never be reached.")
except ValueError as e:
    print(f"   [!] Blocked by descriptor: Caught ValueError -> {e}")

print("\n Attempting to create a new student with an invalid initial grade (-15)...")
try:
    invalid_student = Student("Bad Student", "CS-41", -15.0)
except ValueError as e:
    print(f"   [!] Blocked during __init__: Caught ValueError -> {e}")


print("\n[Explanations]")

print('''We see that assigning a valid grade works normally. However, assigning an out-of-bounds value (like
       120 or -15) immediately triggers a `ValueError` with a descriptive message. This validation works 
      both when modifying an existing object and when creating a completely new `Student`.''')

print('''It works because we implemented the Descriptor Protocol (`__get__`, `__set__`, `__set_name__`) 
      in the `GradeDescriptor` class and assigned it to the `grade` class attribute in `Student`. In Python,
       whenever we access or assign a value to `student.grade`, the interpreter detects the descriptor and 
      redirects the operation. Our `__set__` method intercepts the assignment, validates the range (0-100), 
      and rejects invalid values before they can be stored in the object's dictionary.''')


#Task D — Integration
print("\n-----Task D — Integration-----\n")

initial_students: list[Student] = [
    Student("John Smith", "Group-1", 42.5),
    Student("John Doe", "Group-2", 66.6),
    Student("Jane Doe", "Group-1", 83.2)
]

print("Executing the integrated block:\n")

try:
    with StudentCollection(initial_students) as collection:
        for student in collection:
            print(f"Iterating: {student.name} has grade {student.grade}")
            
            if student.name == "Jane Doe":
                print(f"\n  -> Attempting to update {student.name}'s grade to 150.0...")
                student.grade = 150.0

except ValueError as e:
    print(f"\n[Validation Blocked] {e}")


print("\n[Explanations]")

print("1. Context Manager Works: The '>>> Entering...' and '<<< Exiting...' messages are printed.")
print("2. Iteration Works: The `for` loop successfully goes through the collection, accessing each `Student` object.")
print('''3. Descriptor Works: When we try to assign an invalid grade (150.0) to Ivan inside the loop, it 
      instantly raises a `ValueError`, which halts the block, triggers `__exit__`, and is caught by our 
      `except` clause.''')

print('''Because all three Python protocols seamlessly integrate. The `with` statement utilizes the Context 
      Manager protocol (`__enter__`/`__exit__`). Inside the block, the `for` loop utilizes the Iterator 
      protocol (`__iter__`/`__next__`). Finally, when we access or modify `student.grade`, Python transparently 
      redirects the operation to the Descriptor protocol (`__get__`/`__set__`) defined in `GradeDescriptor`.''')

