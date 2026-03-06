import copy
import sys

# Task A: Binding / Rebiding
print("Task A: Binding / Rebiding: \n")

a1 = 3
b1 = a1

print(f"Initial: \na: {a1} ID a: {id(a1)} \nb: {b1} ID b: {id(b1)}\n")

a1 = 2

print(f"After rebiding: \na: {a1} ID a: {id(a1)} \nb: {b1} ID b: {id(b1)}\n")

# Task B: Mutation vs Rebinding
print("Task B: Mutation vs Rebinding \n")

a2 = [5,6]
b2 = a2

print(f"Initial: \na: {a2} ID a: {id(a2)} \nb: {b2} ID b: {id(b2)}\n")

a2.append(7)

print(f"After mutation: \na: {a2} ID a: {id(a2)} \nb: {b2} ID b: {id(b2)}\n")

# Task C: Function arguments
print("Task C: Function arguments \n")

def f1(x):
    x.append(1)

def g1(x):
    x = [2]

a3 = [0]

print(f"Initial: \na: {a3}\n")

f1(a3)

print(f"After mutate: \na: {a3}\n")

g1(a3)

print(f"After rebind: \na: {a3}\n")

# Task D: Default argument behavior
print("Task D: Default argument behavior \n")

def f2(x = []):
    x.append(1)
    return x

print(f"First call: {f2()}\n")
print(f"Second call: {f2()}\n")

# Task E: Copy semantics
print("Task E: Copy semantics \n")

a4 = [[1,2]]
b4 = a4.copy()
c4 = copy.deepcopy(a4)

print(f"Original: \na: {a4} \nb: {b4}\nc: {c4} \n")

b4[0].append(3)

print(f"After modifying b: \na: {a4} \nb: {b4}\nc: {c4} \n")

# Task F: Reference counting / GC
print("Task F: Reference counting / GC \n")

def refcount(x):
    return sys.getrefcount(x)

print("Part 1: \n")
a5 = []

print(f"Reference count: {refcount(a5)}\n")

b5 = a5

print(f"Reference count after b = a: {refcount(a5)}\n")

print("Part 2: \n")

print(f"Reference count 5: {refcount(5)}\n")
print(f"Reference count 12345: {refcount(12345)}\n")