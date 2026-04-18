from typing import Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod

#Preparation

class Serializable(Protocol):
    def serialize(self) -> str:
        ...

def export(obj: Serializable) -> None:
 print(obj.serialize())

#Task A — Regular class (duck typing)
print("---Task A — Regular class (duck typing)---\n")

class StudentRegular:
    def __init__(self, name:str, group:str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade
    
    def serialize(self) -> str:
        return f"Student[{self.name}, {self.group}, {self.average_grade}]"


student = StudentRegular("John Smith", "Group-1", 42.5)

print("Calling export() function with StudentRegular object:")
export(student)

#Task B — Dataclass implementation
print("\n---Task B — Dataclass implementation---\n")

@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float
    
    def serialize(self) -> str:
        return f"StudentData[{self.name}, {self.group}, {self.average_grade}]"


student_data = StudentData("Jane Doe", "Group-2", 92.0)

print("Calling export() function with StudentData object:")
export(student_data)

#Task C — Slots
print("\n-----Task C — Slots-----\n")

@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float
    
    def serialize(self) -> str:
        return f"StudentSlots[{self.name}, {self.group}, {self.average_grade}]"


student_slots = StudentSlots("John Doe", "Group-3", 95.0)

print(" Protocol compatibility:")
export(student_slots)

print("\n Internal storage check (does not behave like a dynamic dictionary):")
try:
    print(student_slots.__dict__)
except AttributeError as e:
    print(f"Caught expected error: {e}")
    print("-> Success: __dict__ does not exist because slots are used.")

print("\n Restriction check (adding a new attribute is not allowed):")
try:
    student_slots.age = 20 # type: ignore[attr-defined]
except AttributeError as e:
    print(f"Caught expected error: {e}")
    print("-> Success: Cannot add new attributes dynamically.")

#Task D — ABC version
print("\n-----Task D — ABC version-----\n")

class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade
        
    def serialize(self) -> str:
        return f"StudentABC[{self.name}, {self.group}, {self.average_grade}]"

student_abc = StudentABC("Bob", "Group-1", 78.5)

print(" ABC Demonstration (requires inheritance):")
is_abc = isinstance(student_abc, SerializableABC)
print(f"Is student_abc an instance of SerializableABC? -> {is_abc}")

print("\n Protocol Demonstration (structural subtyping / duck typing):")
export(student_abc)

